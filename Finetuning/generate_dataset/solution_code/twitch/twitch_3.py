import csv
from lxml import etree

# Define the HTML elements and their corresponding XPaths
elements = {
    'element1': {
        'xpath': '//*[@id="element1"]',
        'name': 'Name'
    },
    'element2': {
        'xpath': '//*[@id="element2"]',
        'name': 'Rating'
    }
}

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse('downloaded_pages/twitch.html', parser)

# Retrieve the desired elements from the page
data = []
for element, details in elements.items():
    xpath = details['xpath']
    name = details['name']
    elements = tree.xpath(xpath)
    
    for el in elements:
        value = el.text.strip()
        data.append((name, value))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)