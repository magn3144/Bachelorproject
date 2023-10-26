import csv
from lxml import etree

# Define XPath expressions for product names and prices
product_name_xpath = "//div[@class='h4 grid-view-item__title product-card__title']"
price_xpath = "//span[@class='price-item price-item--regular']"

# Parse the HTML file
tree = etree.parse("downloaded_pages/cbsports.html")

# Find all product names using XPath
product_names = tree.xpath(product_name_xpath)
product_names = [name.text.strip() for name in product_names]

# Find all prices using XPath
prices = tree.xpath(price_xpath)
prices = [price.text.strip() for price in prices]

# Combine product names and prices into a list of tuples
product_data = list(zip(product_names, prices))

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Product Name", "Price"])
    writer.writerows(product_data)