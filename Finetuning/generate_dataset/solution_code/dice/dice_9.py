import csv
from lxml import etree

# Load the HTML file
html_file = 'downloaded_pages/dice.html'
with open(html_file, 'r') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Scrape job IDs
job_ids = tree.xpath('//a[contains(@class, "card-title-link")]/@id')

# Save job IDs as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Job ID'])
    for job_id in job_ids:
        writer.writerow([job_id])