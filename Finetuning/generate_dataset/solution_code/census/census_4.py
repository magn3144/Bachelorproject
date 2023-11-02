import csv
from lxml import html

# Load the HTML file
tree = html.parse('downloaded_pages/census.html')

# Retrieve the page title
title = tree.xpath('/html/head/title/text()')[0]

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Page Title'])
    writer.writerow([title])