import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/arxiv.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the footer link element
footer_link = tree.xpath('/html/body/footer/div/div[1]/div/div[2]/ul/li[2]/a')

# Extract the title of the footer link
title = footer_link[0].text.strip()

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerow([title])