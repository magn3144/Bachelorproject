import csv
import os
from lxml import etree

# Define the target XPath for the desired text
target_xpath = '/html/body/div[4]/div[4]/div[3]/section/div[1]/div[1]/div[2]/h2'

# File path to the downloaded HTML file
html_file_path = 'downloaded_pages/ebay.html'

# Parse the HTML file
tree = etree.parse(html_file_path)

# Find the desired element using the target XPath
element = tree.xpath(target_xpath)[0]

# Extract the text from the element
scraped_text = element.text

# Create a CSV file to store the scraped data
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Scraped Data'])
    writer.writerow([scraped_text])

# Print confirmation message
print('Scraped data has been saved to scraped_data.csv')