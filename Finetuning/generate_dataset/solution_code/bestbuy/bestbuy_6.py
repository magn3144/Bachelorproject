import csv
from lxml import etree

# Define the HTML file path
html_file = 'downloaded_pages/bestbuy.html'

# Define the target XPath for similar product suggestions from outside of Best Buy
xpath = '//h3[contains(text(), "Similar products from outside of Best Buy")]/following-sibling::div/ul/li/span/a'

# Parse the HTML file
tree = etree.parse(html_file)

# Find the relevant elements using XPath
elements = tree.xpath(xpath)

# Extract the text from each element
data = [element.text for element in elements]

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Similar Products'])
    writer.writerow(data)