import csv
from lxml import etree

# Define the local path to the HTML file
html_file = 'downloaded_pages/globestudios.html'

# Define the XPath for the target element
target_xpath = '/html/body/div/div[6]/div/div[2]'

# Load the HTML file
with open(html_file, 'r') as f:
    html_data = f.read()

# Parse the HTML data
html_tree = etree.HTML(html_data)

# Find the target element based on XPath
target_element = html_tree.xpath(target_xpath)[0]

# Retrieve the content from the target element
content = target_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Content'])
    writer.writerow([content])