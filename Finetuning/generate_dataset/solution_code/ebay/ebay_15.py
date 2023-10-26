import csv
from lxml import etree

html_path = 'downloaded_pages/ebay.html'
output_file = 'scraped_data.csv'

def extract_text(xpath):
    tree = etree.parse(html_path)
    element = tree.xpath(xpath)
    if element:
        return element[0].text.strip()
    else:
        return ''

data = {
    'Category': 'E-commerce',
    'Task': 'Extract the text for "Congo, Democratic Republic of the"',
    'Text': extract_text('/html/body/div[4]/div[4]/div[3]/section/div[1]/div[2]/div[1]/div/div/form/div[1]/div/span/div/div[46]/span')
}

with open(output_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)