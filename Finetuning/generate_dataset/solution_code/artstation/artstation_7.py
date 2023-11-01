import csv
from lxml import etree

# Extract lead paragraphs from HTML file using XPath expression
def extract_lead_paragraphs(tree):
    paragraphs = tree.xpath('/html/body/div/div[@class="lead"]')
    return [p.text for p in paragraphs]

# Open the HTML file
with open('downloaded_pages/artstation.html', 'r') as file:
    html = file.read()

# Create an etree from the HTML
tree = etree.HTML(html)

# Extract lead paragraphs
lead_paragraphs = extract_lead_paragraphs(tree)

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Lead Paragraph'])
    writer.writerows([[paragraph] for paragraph in lead_paragraphs])