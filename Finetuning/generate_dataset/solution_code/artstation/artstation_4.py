import csv
import os
from lxml import html

# Read the local HTML file
path = "downloaded_pages/artstation.html"
with open(path, "r", encoding="utf-8") as file:
    content = file.read()

# Create an HTML tree
tree = html.fromstring(content)

# Find all headings with class "bs-modal-title"
headings = tree.xpath("//h3[@class='bs-modal-title']")

# Extract the text from the headings
headings_text = [heading.text.strip() for heading in headings]

# Prepare data for CSV file
data = [["Heading"]]
data.extend([[heading] for heading in headings_text])

# Save data to a CSV file
csv_file = "scraped_data.csv"
with open(csv_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data scraped and saved as 'scraped_data.csv'.")