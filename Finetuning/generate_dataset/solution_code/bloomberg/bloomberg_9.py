import csv
from lxml import etree

# Define the paths to the HTML file and CSV file
html_file = 'downloaded_pages/bloomberg.html'
csv_file = 'scraped_data.csv'

# Define the XPaths for the featured article titles 
xpaths = [
    '/html/body/div[1]/div[2]/div[2]/div[2]/div[5]/div[1]/div/section/section/section/div/div[2]/div[4]/h3',
    '/html/body/div[1]/div[2]/div[2]/div[2]/nav/div[2]/ul/li[2]/ul/li[5]/div/section[1]/article/div[2]/a/h3',
    '/html/body/div[1]/div[2]/div[2]/div[2]/nav/div[2]/ul/li[2]/ul/li[3]/div/section[1]/article/div[2]/a/h3'
]

# Parse the HTML file
tree = etree.parse(html_file)

# Scrape the featured article titles
titles = []
for xpath in xpaths:
    element = tree.xpath(xpath)
    if element:
        titles.append(element[0].text)
    else:
        titles.append('N/A')

# Save the scraped titles as a CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerows(zip(titles))