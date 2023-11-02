import csv
import requests
from lxml import html

# Define the local path to the HTML file
html_file = 'downloaded_pages/stackexchange-hot-questions.html'

# Read the HTML file
with open(html_file, 'r', encoding='utf-8') as file:
    html_data = file.read()

# Parse the HTML content
tree = html.fromstring(html_data)

# Find the Worldbuilding site name using XPath
site_name = tree.xpath('/html/body/div/section/div/div[3]/div[2]/div[5]/div/span[2]/text()')

# Save the site name as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Site Name'])
    writer.writerow(site_name)