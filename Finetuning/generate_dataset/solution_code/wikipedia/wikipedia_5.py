import csv
from pathlib import Path
from lxml import etree

# Define the HTML elements and their corresponding XPaths
elements = {
    'languages': {
        'xpath': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[5]/div[3]/div/ul/li/div[2]/ul/li/a/span',
        'output_key': 'language'
    },
    'article_counts': {
        'xpath': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[5]/div[3]/div/ul/li/div[1]/div[2]',
        'output_key': 'article_count'
    }
}

# Define the path to the HTML file
html_file_path = 'downloaded_pages/wikipedia.html'

# Define the output CSV file path
output_file_path = 'scraped_data.csv'

# Parse the HTML file
tree = etree.parse(html_file_path)
root = tree.getroot()

# Initialize the data list
data = []

# Scrape the required information
for element_key, element_config in elements.items():
    xpath = element_config['xpath']
    output_key = element_config['output_key']

    elements = root.xpath(xpath)
    values = [element.text.strip() for element in elements]

    data.append({output_key: value for value in values})

# Write the scraped data to the CSV file
with open(output_file_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=elements.keys())
    writer.writeheader()
    writer.writerows(data)