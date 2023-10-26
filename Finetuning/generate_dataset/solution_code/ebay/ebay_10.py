import csv
import requests
from lxml import html

# Load the HTML file
with open('downloaded_pages/ebay.html', 'r') as file:
    page_content = file.read()

# Parse the HTML content
tree = html.fromstring(page_content)

# Scrape all scooter parts and accessories
elements = tree.xpath("//a[contains(text(), 'Scooter Parts & Accessories')]")

# Extract the text from the scraped elements
data = [element.text for element in elements]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Scraped Data'])
    writer.writerows(zip(data))