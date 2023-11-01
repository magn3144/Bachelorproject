import csv
from lxml import etree

# Define the local path to the HTML file
html_path = 'downloaded_pages/employmentfirstfl.html'

# Define the XPaths for the h2 tags in the sidebar
sidebar_h2_xpaths = [
    '/html/body/div/div/aside/section/h2',
    '/html/body/div/div/aside/section/div/p[1]/a[1]',
    '/html/body/div/div/aside/section/div/p[3]/a[1]',
    '/html/body/div/div/aside/section/div/p[3]/a[2]',
    '/html/body/div/div/aside/section/div/p[4]/a[2]',
    '/html/body/div/div/aside/section/div/p[4]/a[3]',
    '/html/body/div/div/aside/section/div/p[4]/a[4]',
    '/html/body/div/div/aside/section/div/p[5]/a'
]

# Create a list to store the scraped h2 tags
scraped_data = []

# Parse the HTML file
tree = etree.parse(html_path, etree.HTMLParser())

# Iterate over the sidebar h2 XPaths and extract the text
for xpath in sidebar_h2_xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        scraped_data.append(element.text.strip())

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category', 'Text'])
    for item in scraped_data:
        writer.writerow(['Educational Websites', item])