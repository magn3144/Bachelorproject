import csv
import os
from lxml import etree

# Read the HTML file
html_path = "downloaded_pages/microsoft.html"
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse the HTML content
parser = etree.HTMLParser()
tree = etree.fromstring(html_content, parser)

# Retrieve the product names
product_names = tree.xpath('//a[contains(@class, "c-uhff-link") and text()="Surface Laptop Studio 2"]/text()')

# Save the scraped data as a CSV file
output_path = "scraped_data.csv"
header = ["Product Name"]

# Write the data to the CSV file
with open(output_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(zip(product_names))

print("Scraping completed. The data has been saved as 'scraped_data.csv'.")