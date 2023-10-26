import csv
from lxml import etree

# Path to the HTML file
html_file = 'downloaded_pages/redfin.html'

# XPaths of the title elements
title_xpaths = [
    '/html/head/title'
]

# Function to extract the text from an element using XPath
def extract_text(element, xpath):
    return element.xpath(xpath)[0].text.strip()

# Open the HTML file and parse it
with open(html_file, 'r') as file:
    html = file.read()
    root = etree.HTML(html)

# Extract the titles
titles = [extract_text(root, xpath) for xpath in title_xpaths]

# Write the titles to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerows(zip(titles))