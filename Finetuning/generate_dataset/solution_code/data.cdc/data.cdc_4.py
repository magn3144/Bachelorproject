import csv
from lxml import etree

def extract_disease_names(html_file):
    with open(html_file, 'r') as f:
        content = f.read()
    parser = etree.HTMLParser()
    tree = etree.fromstring(content, parser=parser)
    disease_names = tree.xpath("//span[contains(@class, 'modal-content-name')]/text()")
    return disease_names

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for item in data:
            writer.writerow([item])

html_file = 'downloaded_pages/data.cdc.html'
disease_names = extract_disease_names(html_file)
save_to_csv(disease_names)