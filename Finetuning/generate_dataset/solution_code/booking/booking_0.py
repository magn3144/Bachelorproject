import csv
from lxml import etree

# Parse the HTML file
html_file = 'downloaded_pages/booking.html'
tree = etree.parse(html_file)
root = tree.getroot()

# Get all property names and prices
property_names = root.xpath('//h4[contains(@class, "abf093bdfe")]')
prices = root.xpath('//strong[contains(@class, "bui-price-display__value prco-inline-block-maker-helper")]')

# Prepare data for CSV
data = []
for name, price in zip(property_names, prices):
    name_text = name.text.strip()
    price_text = price.text.strip()
    data.append([name_text, price_text])

# Save data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Property Name', 'Price'])
    writer.writerows(data)