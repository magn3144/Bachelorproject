import csv
from lxml import etree

# Define the target page URL
target_url = "file://localhost/downloaded_pages/bloomberg.html"

# Define the XPaths for the category elements
category_xpath = "/html/body/div[1]/div[2]/div[2]/div[2]//h3[contains(@class, 'article-story__eyebrow')]"

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(target_url, parser)

# Extract the categories
categories = tree.xpath(category_xpath)

# Write the categories to a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Category"])

    for category in categories:
        writer.writerow([category.text])