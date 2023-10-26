import csv
from lxml import etree

# Path to the HTML file
html_file = "downloaded_pages/ebay.html"

# XPath for the target element
xpath = "/html/body/div[3]/header/table/tbody/tr/td[2]/div/div/table/tbody/tr/td[1]/ul[1]/li[3]/a"

# Read the HTML file
with open(html_file, "r") as file:
    html_content = file.read()

# Parse the HTML content
parser = etree.HTMLParser()
tree = etree.parse(html_content, parser)

# Find the target element using XPath
target_element = tree.xpath(xpath)[0]

# Extract the text from the element
text = target_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([text])