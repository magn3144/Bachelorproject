import csv
from lxml import etree

# Define the XPath expressions for the anchor tags and their respective paths
anchor_xpath = '//a'
path_xpath = '//a/@href'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse('downloaded_pages/fifa.html', parser)

# Extract the link texts and paths
links = tree.xpath(anchor_xpath)
paths = tree.xpath(path_xpath)

# Create a CSV file to save the scraped data
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link Text', 'Path'])
    for link, path in zip(links, paths):
        writer.writerow([link.text, path])