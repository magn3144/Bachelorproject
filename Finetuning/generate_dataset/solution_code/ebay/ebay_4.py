import csv
import os
from lxml import html

# Define the HTML elements and their corresponding XPaths
elements = {
    'country_label': {
        'element': 'label',
        'xpath': '/html/body/div[4]/div[4]/div[3]/section/div[1]/div[2]/div[1]/div/div/form/div[1]/div/span/label'
    }
}

# Load the HTML file
file_path = os.path.join('downloaded_pages', 'ebay.html')
with open(file_path, 'r') as file:
    content = file.read()

# Create an element tree from the HTML content
tree = html.fromstring(content)

# Scrape the country label
country_label = tree.xpath(elements['country_label']['xpath'])[0].text

# Save the scraped data as CSV
output_path = 'scraped_data.csv'
with open(output_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Country Label'])
    writer.writerow([country_label])