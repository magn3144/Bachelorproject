import csv
from lxml import etree

# Define the XPath expressions for article titles and authors
title_xpath = "//h3[contains(@class, 'font--headline')]/text()"
author_xpath = "//a[contains(@class, 'wpds-c-knSWeD')]/text()"

# Load the HTML file
html = open('downloaded_pages/washingtonpost.html', 'r').read()

# Parse the HTML content
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Extract the article titles and authors
titles = tree.xpath(title_xpath)
authors = tree.xpath(author_xpath)

# Zip the titles and authors together
data = list(zip(titles, authors))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Author'])
    writer.writerows(data)