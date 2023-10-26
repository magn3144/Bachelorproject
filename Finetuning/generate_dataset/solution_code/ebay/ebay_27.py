import csv
import re
from lxml import etree

# Define the HTML file path
html_path = 'downloaded_pages/ebay.html'

# Define the XPath for the target element
xpath = '/html/body/div[4]/div[4]/div[3]/section/div[1]/div[2]/div[1]/div/div/form/div[1]/div/span/div/div[47]/span'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_path, parser)

# Find the target element using XPath
target_element = tree.xpath(xpath)

# Extract the text from the target element
text = target_element[0].text.strip()

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([text])