import csv
import os
from lxml import etree

# Define the target HTML file
html_file = 'downloaded_pages/employmentfirstfl.html'

# Define the XPaths for the anchor tags in the header
header_anchors_xpath = [
    '/html/body/div/header/div[2]/nav/div/ul/li[1]/a',
    '/html/body/div/header/div[2]/nav/div/ul/li[2]/a',
    '/html/body/div/header/div[2]/nav/div/ul/li[3]/a',
    '/html/body/div/header/div[2]/nav/div/ul/li[4]/a',
    '/html/body/div/header/div[2]/nav/div/ul/li[5]/a'
]

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Find the anchor tags in the header using the XPaths
header_anchors = []
for xpath in header_anchors_xpath:
    anchors = tree.xpath(xpath)
    header_anchors.extend(anchors)

# Extract the text from the anchor tags
anchor_texts = [anchor.text.strip() for anchor in header_anchors]

# Save the scraped data as a CSV file
csv_file = 'scraped_data.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Anchor Text'])
    writer.writerows([[text] for text in anchor_texts])