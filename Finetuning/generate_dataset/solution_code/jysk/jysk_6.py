from lxml import etree
import csv

# Read the HTML file
with open('downloaded_pages/jysk.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML using lxml
html = etree.HTML(html_content)

# Find all input elements
input_elements = html.xpath("//input")

# Extract labels of the input fields
labels = [input_element.attrib.get('placeholder') for input_element in input_elements]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(labels)