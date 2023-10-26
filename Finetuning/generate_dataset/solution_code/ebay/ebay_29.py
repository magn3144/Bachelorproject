import os
import csv
from lxml import html

# Define the HTML file path and target XPath
html_file = 'downloaded_pages/ebay.html'
xpath = '//h3[@class="x-refine__item"][contains(text(),"Show only")]'

# Load the HTML file
with open(html_file, 'r', encoding='utf-8') as file:
    page_source = file.read()

# Parse the HTML
tree = html.fromstring(page_source)

# Find the target element
element = tree.xpath(xpath)

# Check if the element is found
if element:
    # Get the text of the element
    show_only_header = element[0].text.strip()
    
    # Save the scraped data as CSV
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Show Only Header'])
        writer.writerow([show_only_header])
else:
    print('Target element not found.')