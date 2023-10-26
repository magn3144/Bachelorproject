import csv
import os
from lxml import etree

# Define the local path to the HTML file
html_file_path = 'downloaded_pages/ebay.html'

# Define the target XPath for the "Item Location" header
target_xpath = "/html/body/div[4]/div[3]/div[1]/div/div/div/ul[2]/li[6]/div/h3"

# Load the HTML file
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# Find the desired element using the target XPath
item_location_header = tree.xpath(target_xpath)[0].text

# Define the output CSV file name
output_file_name = 'scraped_data.csv'

# Prepare the data to be written to CSV
data = [
    ['Item Location Header'],
    [item_location_header]
]

# Write the data to CSV
with open(output_file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)