import csv
from lxml import etree

# Load the HTML file
with open('downloaded_pages/stackexchange-hot-questions.html', 'r') as file:
    html = file.read()

# Parse the HTML
root = etree.HTML(html)

# Extract the title of the page
title = root.xpath('/html/head/title/text()')[0]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerow([title])