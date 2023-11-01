from lxml import etree
import csv

# Load the HTML file
tree = etree.parse('downloaded_pages/macdonalds.html')

# Define the XPath for the menu item
menu_item_xpath = '/html/body/div/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/section/div[3]/ul/li[2]/a/div/div/div[2]'

# Find the menu item element using the XPath
menu_item_element = tree.xpath(menu_item_xpath)[0]

# Extract the name and description from the menu item element
name = menu_item_element.text.strip()
description = menu_item_element.getparent().getnext().text.strip()

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Description'])
    writer.writerow([name, description])