import csv
from lxml import etree

# Load the HTML file
html_path = 'downloaded_pages/dk.indeed.html'
with open(html_path, 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find all job locations using XPath
locations = tree.xpath('//div[contains(@class, "companyLocation")]/text()')

# Write the locations to a CSV file
csv_path = 'scraped_data.csv'
with open(csv_path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Location'])
    writer.writerows([[location] for location in locations])