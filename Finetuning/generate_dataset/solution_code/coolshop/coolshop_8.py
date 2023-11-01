import csv
from lxml import etree

# Define the HTML file path
html_file = 'downloaded_pages/coolshop.html'

# Define the XPath expressions for the titles and links of baby and children's products
title_xpath = "//a[contains(text(),'Baby og børn') or contains(text(),'Baby- og småbørnslegetøj')]/text()"
link_xpath = "//a[contains(text(),'Baby og børn') or contains(text(),'Baby- og småbørnslegetøj')]/@href"

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Extract the titles and links of baby and children's products
titles = tree.xpath(title_xpath)
links = tree.xpath(link_xpath)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Link'])  # Write header
    writer.writerows(zip(titles, links))  # Write data rows