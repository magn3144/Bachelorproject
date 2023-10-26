import csv
from lxml import etree

# Define the target file path
file_path = 'downloaded_pages/ebay.html'

# Define the XPaths to retrieve the desired elements
header_xpath = "//h2[@class='gh-ar-hdn' and text()='Shop by category']"

# Create an empty list to store the scraped data
scraped_data = []

# Read the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Retrieve the "Shop by category" header element
header_element = html_tree.xpath(header_xpath)

# Extract the text from the header element
if header_element:
    header_text = header_element[0].text.strip()
else:
    header_text = ''

# Append the scraped data to the list
scraped_data.append(header_text)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(scraped_data)