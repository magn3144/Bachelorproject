import csv
from lxml import etree

# Define the XPath for the header element
header_xpath = "/html/body/div/div/header/h1"

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse("downloaded_pages/employmentfirstfl.html", parser)

# Find the header element using XPath
header_element = tree.xpath(header_xpath)[0]

# Get the text of the header element
header_text = header_element.text

# Write the scraped data to a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([header_text])