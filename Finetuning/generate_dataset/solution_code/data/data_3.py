import csv
from lxml import etree

# Load the HTML file
with open('downloaded_pages/data.cdc.html', 'r') as file:
    html = file.read()

# Create an XML tree from the HTML
tree = etree.HTML(html)

# Find all A-Z headings
headings = tree.xpath("//h2[contains(text(), 'A-Z')]")

# Extract the text from the headings
heading_texts = [heading.text.strip() for heading in headings]

# Save the data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Heading'])
    writer.writerows([[heading] for heading in heading_texts])