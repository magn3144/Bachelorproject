import csv
from lxml import etree

# Load the HTML file
html_path = 'downloaded_pages/nasdaq.html'
with open(html_path, 'r') as f:
    content = f.read()

# Create an HTML parser
parser = etree.HTMLParser()

# Parse the HTML content
tree = etree.fromstring(content, parser)

# Find all anchor elements
anchor_elements = tree.xpath('//a')

# Extract the anchor text
anchor_text = [element.text.strip() for element in anchor_elements]

# Save the data to a CSV file
csv_path = 'scraped_data.csv'
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Anchor Text'])
    writer.writerows([[text] for text in anchor_text])