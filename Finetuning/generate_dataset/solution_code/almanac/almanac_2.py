import csv
from lxml import etree

# Define the XPath expressions
title_xpath = "//p[contains(@class, 'prod-title')]/text()"
price_xpath = "//p[contains(@class, 'prod-title')]/following-sibling::p/text()"

# Read the HTML file
with open("downloaded_pages/almanac.html", "r") as file:
    html = file.read()

# Create an ElementTree object
tree = etree.HTML(html)

# Extract the titles and prices
titles = tree.xpath(title_xpath)
prices = tree.xpath(price_xpath)

# Combine the titles and prices into a list of tuples
data = list(zip(titles, prices))

# Save the data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"]) # Write header row
    writer.writerows(data) # Write data rows to the file