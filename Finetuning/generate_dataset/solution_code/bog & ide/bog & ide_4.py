import csv
from lxml import etree

# Define the local path to the HTML file
html_file = "downloaded_pages/bog & ide.html"

# Define the XPath for the category "Lokalhistorie"
category_xpath = '/html/body/div/header/ul/li[1]/ul/li[10]/ul/li[5]/a'

# Read the HTML file
with open(html_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Find the category element using XPath
category_element = html_tree.xpath(category_xpath)[0]

# Get the text of the category element
category = category_element.text

# Save the category as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([category])