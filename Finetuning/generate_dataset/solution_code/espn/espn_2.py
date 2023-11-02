import csv
import os
from lxml import etree

# Set the path to the HTML file
html_file = 'downloaded_pages/espn.html'

# Set the category and website
category = 'Sports Websites'
website = 'espn'

# Set the XPaths for headlines and authors
xpaths = {
    'headlines': [
        {
            'xpath': '/html/body/div[1]/div/div/div/main/div[3]/div/div[2]/div/aside[2]/section/div/div/div[2]/a/div/h2',
            'name': 'headline'
        },
    ],
    'authors': [
        {
            'xpath': '/html/body/div[1]/div/div/div/main/div[3]/div/div[2]/div/aside[2]/section/div/div/div[3]/a/div/ul/li[2]',
            'name': 'author'
        },
    ]  
}

# Create a function to scrape data based on the given XPaths
def scrape_data(file_path, xpaths):
    scraped_data = []
    tree = etree.parse(file_path)

    for key, values in xpaths.items():
        for value in values:
            elements = tree.xpath(value['xpath'])
            data = [element.text.strip() if element.text else '' for element in elements]
            scraped_data.append({'name': value['name'], 'data': data})

    return scraped_data

# Scrape the data
scraped_data = scrape_data(html_file, xpaths)

# Save the scraped data as a CSV file
csv_file = 'scraped_data.csv'

if not os.path.exists(csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['category', 'website', 'name', 'data'])
        writer.writeheader()

with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)
    for data in scraped_data:
        for d in data['data']:
            writer.writerow([category, website, data['name'], d])