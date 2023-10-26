import csv
from lxml import etree

# Define the target HTML file
html_file = "downloaded_pages/britannica.html"

# Define the XPaths for the categories related to animals and nature
xpaths = [
    "/html/body/div[1]/div/div/div/div/a[contains(@class, 'category-link-ANIMALS')]",
    "/html/body/div[1]/div/div/div/div/a[contains(@class, 'category-link-NATURE')]"
]

# Scrape the categories
categories = []
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)
for xpath in xpaths:
    elements = tree.xpath(xpath)
    categories.extend([element.text for element in elements])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Category"])
    writer.writerows([[category] for category in categories])