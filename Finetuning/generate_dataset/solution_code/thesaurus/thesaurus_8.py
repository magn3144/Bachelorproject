import csv
from lxml import etree

# Define the target HTML file path
html_file_path = 'downloaded_pages/thesaurus.html'

# Define the XPaths for the frequently used words
xpaths = [
    '/html/body/div/div/main/div[1]/div[7]/div/ol/li[3]/a',
    '/html/body/div/div/main/div[1]/div[7]/div/ol/li[4]/a',
    '/html/body/div/div/main/div[1]/div[7]/div/ol/li[1]/a',
    '/html/body/div/div/main/div[1]/div[7]/div/ol/li[2]/a',
    '/html/body/div/div/main/div[1]/div[7]/div/ol/li[5]/a',
]

# Create an empty list to store the scraped words
words = []

# Parse the HTML file using lxml etree
tree = etree.parse(html_file_path)

# Scrape the frequently used words using the defined XPaths
for xpath in xpaths:
    element = tree.xpath(xpath)
    if element:
        words.append(element[0].text)

# Create a CSV file to save the scraped data
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Frequently Used Words'])
    writer.writerows([[word] for word in words])