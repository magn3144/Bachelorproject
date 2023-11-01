import csv
from lxml import etree

# Set the file path to the downloaded HTML file
html_file_path = "downloaded_pages/google.html"

# Set the XPaths for the desired elements
doodle_newer_xpath = "/html/body/div[2]/div/a[2]"

# Parse the HTML file
with open(html_file_path, "r") as file:
    html = file.read()
    parser = etree.HTMLParser()
    tree = etree.parse(html, parser)

# Retrieve the newer Doodle ID from the "doodle-newer" element
doodle_newer_element = tree.xpath(doodle_newer_xpath)[0]
newer_doodle_id = doodle_newer_element.get("id")

# Save the scraped data as a CSV file
data = {"Newer Doodle ID": [newer_doodle_id]}
csv_file_path = "scraped_data.csv"

with open(csv_file_path, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)