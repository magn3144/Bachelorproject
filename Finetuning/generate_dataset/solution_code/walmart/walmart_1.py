import csv
import os
from lxml import etree

# Set the path to the HTML file
html_file = "downloaded_pages/walmart.html"

# Set the XPath expressions for the names and prices of the products
product_name_xpath = "//h3[contains(@class, 'f4')]/text()"
product_price_xpath = "//div[contains(@class, 'b black lh-copy f5')]/text()"

# Create a list to store the scraped data
scraped_data = []

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Extract the product names and prices using XPath
product_names = tree.xpath(product_name_xpath)
product_prices = tree.xpath(product_price_xpath)

# Iterate over the extracted data and store it in the scraped_data list
for name, price in zip(product_names, product_prices):
    scraped_data.append([name.strip(), price.strip()])

# Set the path to save the CSV file
csv_file = "scraped_data.csv"

# Check if the directory exists, if not, create it
directory = os.path.dirname(csv_file)
os.makedirs(directory, exist_ok=True)

# Write the scraped data to the CSV file
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price"])
    writer.writerows(scraped_data)