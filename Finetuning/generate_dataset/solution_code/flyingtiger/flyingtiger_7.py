import csv
from lxml import etree

# Load the HTML file
html_file = 'downloaded_pages/flyingtiger.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse the HTML content
parser = etree.HTMLParser()
tree = etree.fromstring(html_content, parser)

# Find all <h4> tags and extract the text
h4_elements = tree.xpath('//h4')
h4_texts = [element.text.strip() for element in h4_elements]

# Save the scraped data as a CSV file
output_file = 'scraped_data.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['H4 Text'])
    writer.writerows([[text] for text in h4_texts])