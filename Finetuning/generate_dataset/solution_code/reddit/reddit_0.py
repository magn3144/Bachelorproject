import csv
from lxml import etree

# Define the HTML elements and their XPaths
elements = {
    "<title>(83) Update on $50k NVDA Puts : wallstreetbets</title>": "/html/head/title"
}

# Open the HTML file and parse it using lxml
with open("downloaded_pages/reddit.html", "r") as file:
    html = file.read()

parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Scrape the target data using the XPaths
scraped_data = []
for element, xpath in elements.items():
    element_data = tree.xpath(xpath)
    if element_data:
        scraped_data.append([element, element_data[0].text])

# Save the scraped data as CSV
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(scraped_data)