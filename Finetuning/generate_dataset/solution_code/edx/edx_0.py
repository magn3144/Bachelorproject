import csv
import requests
from lxml import html

# Read the local HTML file
with open('downloaded_pages/edx.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find the link using XPath
link = tree.xpath('//a[contains(text(),"Browse online artificial intelligence courses")]/text()')[0]

# Save the link as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([link])