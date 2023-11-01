import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/top.html', 'r') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all h5 elements
h5_elements = tree.xpath('//h5')

# Extract the text from h5 elements
text_data = [element.text for element in h5_elements]

# Save the text data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(zip(text_data))