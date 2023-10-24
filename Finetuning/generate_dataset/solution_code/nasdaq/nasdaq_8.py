import csv
from lxml import etree

# Define the path to the HTML file
html_file = 'downloaded_pages/nasdaq.html'

# Define the XPaths for the desired elements
xpaths = [
    '/html/body/div[2]/div/main/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[5]/div[1]/div/table/tbody/tr/td/div',
    '/html/body/div[2]/div/main/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[5]/div[1]/div/table/tbody/tr/td/div',
    '/html/body/div[2]/div/main/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[5]/div[1]/div/table/tbody/tr/td/div'
]

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Scrape the values using the XPaths
values = []
for xpath in xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        values.append(element.text)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Value'])
    writer.writerows([[value] for value in values])