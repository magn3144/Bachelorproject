import csv
from lxml import etree

# Define the XPath expressions for the form submission buttons
buttons_xpath = [
    "/html/body//button[@type='submit']/text()",
    "//input[@type='submit']/@value",
    "//input[@type='image']/@alt"
]

# Load the HTML file
with open('downloaded_pages/careerbuilder.html', 'r') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Scrape the form submission buttons
buttons = []
for xpath in buttons_xpath:
    buttons.extend(tree.xpath(xpath))

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Button Text'])
    writer.writerows([[button] for button in buttons])