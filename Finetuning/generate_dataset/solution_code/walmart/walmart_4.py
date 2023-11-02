import csv
import requests
from lxml import html

# Read the HTML file
with open('downloaded_pages/walmart.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content
tree = html.fromstring(content)

# Get the names and descriptions of all salad kits
salad_kits = tree.xpath('//h3[contains(@class, "f4") or contains(@class, "f3-m")]/text()')
descriptions = tree.xpath('//h3[contains(@class, "f4") or contains(@class, "f3-m")]/following-sibling::p/text()')

# Combine the names and descriptions into a list of dictionaries
data = [{'Name': kit, 'Description': desc} for kit, desc in zip(salad_kits, descriptions)]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Description'])
    writer.writeheader()
    writer.writerows(data)