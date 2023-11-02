import csv
from lxml import etree

html_file = "downloaded_pages/finance.yahoo.html"

# Define the XPaths for the search label
search_label_xpath = "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div/form/label"

# Read the HTML file
with open(html_file, "r") as f:
    html_content = f.read()

# Parse the HTML content
parser = etree.HTMLParser()
tree = etree.fromstring(html_content, parser)

# Scrape the search label using XPath
search_label = tree.xpath(search_label_xpath)[0].text

# Save the scraped data as CSV
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([search_label])