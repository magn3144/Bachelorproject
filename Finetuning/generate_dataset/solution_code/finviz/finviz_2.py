import csv
from lxml import html

# Define the HTML elements and their XPaths
elements = [
    {
        'name': 'Title',
        'xpath': '/html/head/title'
    },
    {
        'name': 'Timestamp',
        'xpath': '/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[13]/div/div/div/div/span'
    }
]

# Load the HTML file
with open('downloaded_pages/finviz.html', 'r') as file:
    content = file.read()

# Parse the HTML content
tree = html.fromstring(content)

# Scrape the data and store in a dictionary
data = {}
for element in elements:
    xpath = element['xpath']
    element_text = tree.xpath(xpath)
    if element_text:
        data[element['name']] = element_text[0].text

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data.keys())
    writer.writerow(data.values())