import csv
from lxml import etree

# Define the XPath expressions for the product titles and prices
title_xpath = "//span[contains(@class, 'text-variation') and contains(., 'PlayStation')]/text()"
price_xpath = "//div[contains(@class, 'pricing-price__regular-price')]/text()"

# Load the HTML file
html_file = 'downloaded_pages/bestbuy.html'
with open(html_file, 'r') as file:
    html_data = file.read()

# Parse the HTML data
html_tree = etree.HTML(html_data)

# Extract the product titles and prices
titles = html_tree.xpath(title_xpath)
prices = html_tree.xpath(price_xpath)

# Create a list of dictionaries representing the scraped data
scraped_data = []
for title, price in zip(titles, prices):
    scraped_data.append({'Title': title.strip(), 'Price': price.strip()})

# Save the scraped data as a CSV file
csv_file = 'scraped_data.csv'
csv_columns = ['Title', 'Price']
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(scraped_data)