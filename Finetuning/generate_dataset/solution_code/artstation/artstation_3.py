import csv
from lxml import etree

# Define the HTML path
html_path = 'downloaded_pages/artstation.html'

# Define the XPaths for currency codes
currency_xpath = [
    '/html/body/div[1]/nav/ul/ul[2]/li[3]/button/span/div[1]',
    '/html/body/div[1]/nav/div[1]/ul/li[6]/div/ul/li[3]/button/span[2]',
    '/html/body/div[1]/nav/div[1]/ul/li[6]/button/span/div[1]'
]

# Parse the HTML file
tree = etree.parse(html_path)

# Initialize the list to store currency codes
currency_codes = []

# Extract currency codes using XPaths
for xpath in currency_xpath:
    elements = tree.xpath(xpath)
    for element in elements:
        currency_codes.append(element.text.strip())

# Save the currency codes as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Currency Code'])
    writer.writerows([[code] for code in currency_codes])