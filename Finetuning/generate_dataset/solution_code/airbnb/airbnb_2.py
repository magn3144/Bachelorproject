import requests
from lxml import etree
import csv

# Read local HTML file
with open('downloaded_pages/airbnb.html', 'r') as file:
    html = file.read()

# Parse HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find elements using XPaths and extract text
elements = [
    tree.xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[7]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div'),
    tree.xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/h1/div[1]/a/span'),
    tree.xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[19]/div/div[2]/div/div/div/div/div/div[2]/span/span[2]')
]

# Prepare data for CSV
data = [
    ['Category', 'Text'],
    ['Tourism', elements[0][0].text],
    ['Tourism', elements[1][0].text],
    ['Tourism', elements[2][0].text],
]

# Save data to CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)