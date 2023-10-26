import csv
from lxml import etree

# Define the XPath for the open house information
open_house_xpath = "//span[contains(text(), 'Open houses')]/../../ul/li/a/span"

# Parse the HTML file
tree = etree.parse('downloaded_pages/redfin.html')

# Find all the open house elements using the XPath
open_house_elements = tree.xpath(open_house_xpath)

# Extract the text from each open house element
open_house_info = [element.text.strip() for element in open_house_elements]

# Write the scraped data to a CSV file
with open('scraped_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Open House Information'])
    writer.writerows([[info] for info in open_house_info])