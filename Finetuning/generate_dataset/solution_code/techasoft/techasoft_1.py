import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/techasoft.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all the forums and review sites
elements = tree.xpath('//a[starts-with(@href, "http") and contains(@href, "forum") or contains(@href, "review")]')

# Create a list to store the data
data = []
for element in elements:
    name = element.text.strip()
    link = element.get('href')
    data.append([name, link])

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)