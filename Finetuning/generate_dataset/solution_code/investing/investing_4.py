import csv
from lxml import etree

# Define the HTML file path
html_file = 'downloaded_pages/investing.html'

# Define the XPaths for cryptocurrency symbols and price changes
xpath_symbols = '//div[contains(@class, "crypto-coins-table_cellNameText__aaXmK")]/text()'
xpath_changes = '//td[contains(@class, "datatable_cell--align-end__qgxDQ")]/text()'

# Parse the HTML file
with open(html_file, 'r', encoding='utf-8') as file:
    html_data = file.read()
    tree = etree.HTML(html_data)

# Extract the cryptocurrency symbols and price changes using the XPaths
symbols = tree.xpath(xpath_symbols)
changes = tree.xpath(xpath_changes)

# Combine the symbols and changes into a list of tuples
data = list(zip(symbols, changes))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Symbol', 'Price Change'])
    writer.writerows(data)