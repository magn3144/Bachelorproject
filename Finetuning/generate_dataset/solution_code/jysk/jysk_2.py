import csv
from lxml import etree

# Define the target HTML file path
html_path = 'downloaded_pages/jysk.html'

# Define the XPaths for the category elements
category_xpaths = [
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[5]/div/div[2]/div/div[1]/article/div[1]/h2/a',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[4]/div/div/div[1]/p',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[4]/div/div/div[1]/p',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[3]/div/div/div[2]/div/div[4]/a/span[1]/span',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[3]/div/div/div[2]/div/div[6]/a/span[1]/span'
]

# Initialize the list to hold the scraped categories
scraped_data = []

# Parse the HTML file
tree = etree.parse(html_path)

# Scrape the categories using the XPaths
for xpath in category_xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        category = element.text.strip()
        scraped_data.append(category)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category'])
    writer.writerows([[category] for category in scraped_data])