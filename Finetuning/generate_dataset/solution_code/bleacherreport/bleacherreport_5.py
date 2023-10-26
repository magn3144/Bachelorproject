import csv
import os
from lxml import html

# Parse the HTML file
file_path = "downloaded_pages/bleacherreport.html"
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
tree = html.fromstring(content)

# Extract the categories from the articles
categories = tree.xpath("//a[contains(@class, 'typography')]/text()")

# Save the data as a CSV file
csv_file = "scraped_data.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Category"])
    writer.writerows([[category] for category in categories])

print("Scraped data saved successfully as 'scraped_data.csv'.")