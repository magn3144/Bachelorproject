import csv
from lxml import etree

# Define the XPath expressions for the elements to scrape
product_description_xpath = "//*[@class='product-description']"
product_specifications_xpath = "//*[@class='product-specifications']"
product_features_xpath = "//*[@class='product-features']"

# Open the HTML file
with open('downloaded_pages/normal.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Find all product descriptions
product_descriptions = html_tree.xpath(product_description_xpath)

# Find all product specifications
product_specifications = html_tree.xpath(product_specifications_xpath)

# Find all product features
product_features = html_tree.xpath(product_features_xpath)

# Zip the scraped data together
scraped_data = zip(product_descriptions, product_specifications, product_features)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Description', 'Specifications', 'Features'])  # Write the header
    writer.writerows(scraped_data)