import csv
from lxml import etree

# Define the HTML path
html_path = 'downloaded_pages/bodybuilding.html'

# Define the XPaths and durations
xpaths = [
    '/html/body/section/main/div[3]/div[2]/div/div/div/div/div[2]/div/div[29]/figure/a/figcaption/div[1]/span',
    '/html/body/section/main/div[3]/div[2]/div/div/div/div/div[2]/div/div[32]/figure/a/figcaption/div[2]/span[2]',
    '/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[5]/figure/a/figcaption/div[1]/span',
    '/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[21]/figure/a/figcaption/div[2]/span[2]',
    '/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[31]/figure/a/figcaption/div[1]/span',
    '/html/body/section/main/div[6]/div[2]/div/div/div/div/div[2]/div/div[6]/figure/a/figcaption/div[2]/span[3]',
    '/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[20]/figure/a/figcaption/div[1]/span',
    '/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[18]/figure/a/figcaption/div[1]/span',
]

# Create a list to store the scraped data
scraped_data = []

# Parse the HTML file
with open(html_path, 'rb') as f:
    tree = etree.parse(f)

# Scrape the program durations using the XPaths
for xpath in xpaths:
    duration = tree.xpath(xpath)[0].text.strip()
    scraped_data.append({'XPath': xpath, 'Duration': duration})

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    fieldnames = ['XPath', 'Duration']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)