import csv
import re
from selenium import webdriver

# Specify the location of the downloaded HTML file
path = "downloaded_pages/data.cdc.html"

# Load the HTML file
with open(path, 'r', encoding='utf-8') as file:
    html = file.read()

# Extract the updated label text using regular expressions
updated_label = re.search(r'<div class="browse2-result-timestamp-label">(.*?)</div>', html)
if updated_label:
    updated_text = updated_label.group(1).strip()
else:
    updated_text = ""

# Save the extracted data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Updated Label'])
    writer.writerow([updated_text])