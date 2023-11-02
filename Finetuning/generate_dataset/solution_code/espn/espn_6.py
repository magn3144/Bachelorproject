import csv
from lxml import etree

# Define the target HTML file path
html_path = 'downloaded_pages/espn.html'

# Define the XPaths for captions and descriptions
caption_xpath = "//span[@class='vjs-control-text']"
description_xpath = "//p[@class='vjs-modal-dialog-description vjs-control-text']"

# Parse the HTML file
tree = etree.parse(html_path)

# Find the captions
captions = tree.xpath(caption_xpath)

# Find the descriptions
descriptions = tree.xpath(description_xpath)

# Prepare the data as a list of tuples
data = list(zip(captions, descriptions))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Caption', 'Description'])
    writer.writerows(data)