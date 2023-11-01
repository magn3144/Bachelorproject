import csv
from lxml import etree

# Define the HTML file path
html_file = "downloaded_pages/normal.html"

# Define the XPaths for product names, categories, and prices
product_name_xpath = "//div[@class='product-name']/a/text()"
category_xpath = "//div[@class='category']/a/text()"
price_xpath = "//div[@class='price']/span/text()"

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Extract the data using XPaths
product_names = tree.xpath(product_name_xpath)
categories = tree.xpath(category_xpath)
prices = tree.xpath(price_xpath)

# Combine the extracted data into rows
rows = zip(product_names, categories, prices)

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product Name', 'Category', 'Price'])
    writer.writerows(rows)