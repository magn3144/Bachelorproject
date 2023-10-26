import csv
import re
from lxml import etree

# Load HTML file
with open('downloaded_pages/seekingalpha.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse HTML
tree = etree.HTML(html)

# Find article tags in the Stocks category
article_tags = tree.xpath("//article[contains(@class, 'category-stocks')]")

# Extract data from article tags
data = []
for tag in article_tags:
    title = tag.xpath(".//h3/a")[0].text
    link = tag.xpath(".//h3/a/@href")[0]
    data.append([title, link])

# Save data to CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link'])
    writer.writerows(data)