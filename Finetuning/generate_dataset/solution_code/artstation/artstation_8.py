import csv
from lxml import etree

html_file = 'downloaded_pages/artstation.html'
category = 'Digital Websites'

tree = etree.parse(html_file)

currency_codes = []
nav_elements = tree.xpath("//nav//span[contains(@class, 'currency-code')]")
for element in nav_elements:
    currency_codes.append(element.text.strip(','))

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Currency Code'])
    writer.writerow([category, ''])
    for code in currency_codes:
        writer.writerow(['', code])