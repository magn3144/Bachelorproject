import csv
import os
from lxml import etree

# Define the target page file path
file_path = 'downloaded_pages/walmart.html'

# Define the XPath for the Thanksgiving-related products
xpath = "/html/body/div/div[1]/div/div/div[1]/div/div[1]/section[2]/nav/ul/li[3]/a"

# Load the HTML file
with open(file_path, 'r') as f:
    html = f.read()

# Parse the HTML
tree = etree.HTML(html)

# Find the Thanksgiving-related products using XPath
products = tree.xpath(xpath)

# Extract the names of the products
product_names = [product.text for product in products]

# Define the CSV file path
output_path = 'scraped_data.csv'

# Write the product names to the CSV file
with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Product Name'])
    writer.writerows([[name] for name in product_names])