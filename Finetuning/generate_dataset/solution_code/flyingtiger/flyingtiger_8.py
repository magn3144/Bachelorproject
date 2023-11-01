import csv
from lxml import etree

# Read the HTML file
html_file = 'downloaded_pages/flyingtiger.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Find all <h6> tags and extract the text
h6_elements = tree.xpath('//h6')
h6_text_list = [element.text.strip() for element in h6_elements]

# Save the scraped data as a CSV file
csv_file = 'scraped_data.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Text'])
    writer.writerows([[text] for text in h6_text_list])