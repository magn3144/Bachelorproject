import csv
from pathlib import Path
from lxml import etree

# Define the local path to the HTML file
path_to_html = Path("downloaded_pages/h&m.html")

# Define the target XPaths for the category name
category_name_xpath = "/html/body/div/div[3]/main/h1"

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(str(path_to_html), parser)

# Get the category name
category_name_element = tree.xpath(category_name_xpath)
category_name = category_name_element[0].text if category_name_element else ""

# Save the category name as a CSV file
with open("scraped_data.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category"])
    writer.writerow([category_name])
