import csv
from lxml import etree

# Define the HTML file path
html_file = 'downloaded_pages/aljazeera.html'

# Define the XPath expressions for the navigation menu items
xpath_expr = "/html/body/div[1]/div/div[2]/div[1]/div/header/nav/ul/li/a"

# Parse the HTML file
tree = etree.parse(html_file)

# Get all navigation menu items
menu_items = tree.xpath(xpath_expr)

# Extract the text from each menu item
menu_item_texts = [item.text for item in menu_items]

# Write the scraped data to CSV file
with open('scraped_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Navigation Menu Items'])
    writer.writerows(zip(menu_item_texts))