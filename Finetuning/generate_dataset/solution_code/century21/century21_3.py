import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/century21.html', 'r') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Define a list to store the scraped descriptions
descriptions = []

# Scrape the descriptions
elements = tree.xpath('//div[contains(@class, "property-card-attribution")]')
for element in elements:
    description = element.text.strip()
    descriptions.append(description)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Description'])
    writer.writerows([[description] for description in descriptions])