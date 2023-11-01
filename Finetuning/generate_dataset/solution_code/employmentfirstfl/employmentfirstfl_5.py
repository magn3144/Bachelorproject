import csv
from lxml import etree

def extract_text_from_anchor_tags(file_path):
    tree = etree.parse(file_path)
    root = tree.getroot()
    anchor_tags = root.xpath("//footer//a")

    data = []
    for tag in anchor_tags:
        text = tag.text.strip()
        data.append(text)

    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Text'])
        writer.writerows([[text] for text in data])

file_path = 'downloaded_pages/employmentfirstfl.html'
extract_text_from_anchor_tags(file_path)