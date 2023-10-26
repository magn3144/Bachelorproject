import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/amazon.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Retrieve all product names
product_names = tree.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]/text()')

# Retrieve all product prices
product_prices = tree.xpath('//span[@class="a-price-symbol"]//following-sibling::span/text()')

# Create a list of tuples for each product (name, price)
products = list(zip(product_names, product_prices))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Price'])
    writer.writerows(products)