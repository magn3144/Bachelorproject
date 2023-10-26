import csv
from lxml import etree

# Define the target HTML file path
html_file_path = 'downloaded_pages/etsy.html'

# Define the XPaths for the HTML elements
element_xpaths = {
    'title': '/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div/div[4]/div[1]/h2'
}

# Function to extract the text content using XPath
def extract_text(element_xpath):
    tree = etree.parse(html_file_path)
    element = tree.xpath(element_xpath)[0]
    return element.text.strip() if element.text else ''

# Extract the title text content using the XPath
title = extract_text(element_xpaths['title'])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title'])
    writer.writerow([title])