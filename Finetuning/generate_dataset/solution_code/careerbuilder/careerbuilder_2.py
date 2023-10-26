import csv
from lxml import etree

# Open HTML file and parse the content
with open('downloaded_pages/careerbuilder.html', 'r') as f:
    html_content = f.read()

parser = etree.HTMLParser()
tree = etree.fromstring(html_content, parser)

# Extract all the text within the heading tags
headings = tree.xpath('//h1 | //h2 | //h3 | //h4')
heading_texts = [heading.text for heading in headings]

# Save the scraped data as CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([[text] for text in heading_texts])