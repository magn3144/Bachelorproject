import csv
from lxml import etree

def extract_text(element):
    if element.tag in ['h1', 'h2', 'h3', 'h4', 'h5']:
        return element.text.strip()
    return ''

def extract_path(element):
    return etree.ElementTree(element).getpath(element)

html_file_path = 'downloaded_pages/ppubs.html'
output_file_path = 'scraped_data.csv'

tree = etree.parse(html_file_path)
root = tree.getroot()

rows = []
for element in root.iter():
    text = extract_text(element)
    if text:
        path = extract_path(element)
        rows.append([text, path])

with open(output_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)