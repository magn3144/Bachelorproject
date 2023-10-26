import csv
from lxml import etree

# Read the HTML file
html_file = 'downloaded_pages/data.cdc.html'
with open(html_file, 'r', encoding='utf-8') as file:
    html_data = file.read()

# Parse the HTML
html_tree = etree.HTML(html_data)

# Find all the tags on the page
tags = html_tree.xpath('//*/text()')

# Save the tags as a CSV file
csv_file = 'scraped_data.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Tags'])

    for tag in tags:
        writer.writerow([tag.strip()])