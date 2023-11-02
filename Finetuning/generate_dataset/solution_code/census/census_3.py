import csv
import requests
from lxml import html

# Set the URL and local file path
url = 'https://www.census.gov/'
file_path = 'downloaded_pages/census.html'

# Read the HTML file
with open(file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find all dataset tags using XPaths
dataset_tags = tree.xpath('//span[contains(@class, "uscb-tag-label")]/text()')

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Dataset Tags'])
    writer.writerows([[tag] for tag in dataset_tags])