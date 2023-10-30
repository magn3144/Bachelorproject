import csv
from lxml import etree

# Load HTML file
html_file = 'downloaded_pages/h&m.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Parse HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find h3 tag with class "fa226d af6753 f4232a"
h3_tags = tree.xpath('//h3[@class="fa226d af6753 f4232a"]')

# Extract text content of h3 tags
h3_texts = [tag.text for tag in h3_tags]

# Save scraped data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Text'])
    writer.writerows([[text] for text in h3_texts])