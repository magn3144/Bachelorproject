import csv
from lxml import etree

# Define the target HTML file path
html_file_path = "downloaded_pages/danielilett.html"

# Define the XPaths
xpaths = {
    "special_thanks": [
        ("/html/body/div[3]/div/div/article/h4[1]", "Special Thanks")
    ]
}

# Create a list to store the scraped data
scraped_data = []

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file_path, parser)

# Scrape special thanks information
for xpath, label in xpaths["special_thanks"]:
    elements = tree.xpath(xpath)
    for element in elements:
        scraped_data.append((label, element.text.strip()))

# Save the scraped data as a CSV file
with open("scraped_data.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Label", "Special Thanks Information"])
    writer.writerows(scraped_data)