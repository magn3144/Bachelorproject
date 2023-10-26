import csv
from lxml import etree

# Set the local path to the HTML file
html_path = 'downloaded_pages/foxnews.html'

# Define the XPaths for the navigation menu items
menu_xpath = [
    '/html/body/div/header/div[4]/div[2]/div/nav/h4/a',
    '/html/body/div/header/div[4]/div[2]/div/nav/h5/a',
    '/html/body/div/footer/div[1]/div/nav/h4/a',
    '/html/body/div/footer/div[1]/div/nav/h5/a'
]

# Create a list to store the scraped data
scraped_data = []

# Parse the HTML file
with open(html_path, 'r') as file:
    html = file.read()
    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)

    # Extract the navigation menu items using the XPaths
    for xpath in menu_xpath:
        items = tree.xpath(xpath)
        for item in items:
            name = item.text.strip()
            scraped_data.append({'Name': name, 'XPath': xpath})

# Save the scraped data as a CSV file
csv_path = 'scraped_data.csv'
fieldnames = ['Name', 'XPath']

with open(csv_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)