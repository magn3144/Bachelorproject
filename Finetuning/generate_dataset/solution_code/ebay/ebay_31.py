import csv
from lxml import etree

# define the target elements and their XPaths
elements = {
    'text': {
        'xpath': '/html/body/div[4]/div[4]/div[3]/section/div[1]/div[2]/div[1]/div/div/form/div[1]/div/span/div/div[171]/span',
        'name': 'Saint Vincent and the Grenadines'
    }
}

# parse the HTML file
tree = etree.parse('downloaded_pages/ebay.html')

# initialize the scraped data
scraped_data = {key: None for key in elements}

# scrape the data from the target elements
for key, value in elements.items():
    element = tree.xpath(value['xpath'])
    if element:
        scraped_data[key] = element[0].text

# save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(scraped_data.keys())
    writer.writerow(scraped_data.values())