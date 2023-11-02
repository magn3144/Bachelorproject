import csv
from lxml import etree

# Define XPath expressions for the merchant tools names and descriptions
names_xpath = '//li[contains(@class, "sub-menu-header")]/text()'
descriptions_xpath = '//li[contains(@class, "sub-menu-header")]/following-sibling::li/text()'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse('downloaded_pages/merchantcircle.html', parser)

# Extract the names and descriptions using XPath expressions
names = tree.xpath(names_xpath)
descriptions = tree.xpath(descriptions_xpath)

# Combine the names and descriptions into a list of dictionaries
data = [{'Name': name.strip(), 'Description': description.strip()} for name, description in zip(names, descriptions)]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csv_file:
    fieldnames = ['Name', 'Description']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)