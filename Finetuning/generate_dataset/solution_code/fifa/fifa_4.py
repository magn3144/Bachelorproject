import csv
from lxml import etree

# Define the local path to the HTML file
local_path = 'downloaded_pages/fifa.html'

# Define the XPaths for the menu items
menu_item_xpaths = [
    '/html/body/div/div/div[1]/header/div[1]/div/div/div[3]/nav/div[4]/div[2]/div[2]/div/div[2]/a',
    '/html/body/div/div/div[1]/header/div[1]/div/div/div[3]/nav/div[4]/div[2]/div[2]/div/div[5]/a',
    '/html/body/div/div/div[1]/header/div[1]/div/div/div[3]/nav/div[3]/div[1]',
    '/html/body/div/div/div[1]/header/div[1]/div/div/div[3]/nav/div[3]/div[2]/div[2]/div/div[2]/a',
    '/html/body/div/div/div[1]/header/div[1]/div/div/div[3]/nav/div[5]/div[2]/div[2]/div/div[2]/a',
    '/html/body/div/div/div[1]/header/div[1]/div/div/div[3]/nav/div[4]/div[1]',
    '/html/body/div/div/div[1]/header/div[1]/div/div/div[3]/nav/div[6]/div[2]/div[2]/div/div[1]/a',
    '/html/body/div/div/div[1]/header/div[1]/div/div/div[3]/nav/div[7]/div[1]',
    '/html/body/div/div/div[1]/header/div[1]/nav/div[4]/a'
]

# Scrape the web page using the local path
with open(local_path, 'r') as file:
    page_content = file.read()

# Create an ElementTree object from the page content
tree = etree.HTML(page_content)

# Initialize a list to store the menu items
menu_items = []

# Extract the menu items using the XPaths
for xpath in menu_item_xpaths:
    menu_item = tree.xpath(xpath)
    if menu_item:
        menu_items.append(menu_item[0].text)
    else:
        menu_items.append('')

# Write the menu items to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Menu Items'])
    writer.writerows(zip(menu_items))