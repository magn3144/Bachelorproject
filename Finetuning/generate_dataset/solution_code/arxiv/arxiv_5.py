import csv
from lxml import etree

# Define the HTML elements and their XPaths
elements = [
    {'name': 'secondary_heading', 'xpath': '/html/body/div[4]/div/h2'}
]

# Load the HTML file
html_file = 'downloaded_pages/arxiv.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Create an element tree from the HTML
tree = etree.HTML(html)

# Scrape the data
data = {}
for element in elements:
    xpath = element['xpath']
    result = tree.xpath(xpath)
    if result:
        data[element['name']] = result[0].text.strip()
    else:
        data[element['name']] = ''

# Save the data as a CSV file
csv_file = 'scraped_data.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)