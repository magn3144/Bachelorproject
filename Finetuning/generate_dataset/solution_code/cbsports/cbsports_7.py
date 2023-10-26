import csv
import requests
from lxml import html

# Define the URL and local path to the HTML file
url = 'https://cbsports.com'
local_path = 'downloaded_pages/cbsports.html'

# Parse the HTML content
with open(local_path, 'r') as f:
    content = f.read()
tree = html.fromstring(content)

# Extract the text from all list items
list_items = tree.xpath('//li/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for item in list_items:
        writer.writerow([item])