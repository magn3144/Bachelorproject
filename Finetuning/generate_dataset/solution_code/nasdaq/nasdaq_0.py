import csv
from lxml import etree

# Define the path to the HTML file
path = "downloaded_pages/nasdaq.html"

# Load the HTML file
with open(path, "r", encoding="utf-8") as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all title elements
titles = tree.xpath("//title/text()")

# Save the titles to a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for title in titles:
        writer.writerow([title])