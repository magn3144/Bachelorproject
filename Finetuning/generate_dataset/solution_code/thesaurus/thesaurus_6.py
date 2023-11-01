import csv
from lxml import etree

def get_data_from_html(html_path):
    with open(html_path, 'r') as f:
        html = f.read()
    tree = etree.HTML(html)

    glossary_elements = tree.xpath('//a[contains(@class, "swOceu30Ur0oywqmOgSd")]/text()')
    glossary_diff_elements = tree.xpath('//a[contains(@class, "swOceu30Ur0oywqmOgSd")]/@href')

    data = []
    for i in range(len(glossary_elements)):
        glossary_text = glossary_elements[i].strip()
        glossary_diff = "N/A"
        diff_element = glossary_diff_elements[i]
        if diff_element.startswith("#"):
            glossary_diff = tree.xpath(f'//a[@href="{diff_element}"]/text()')[0].strip()
        data.append([glossary_text, glossary_diff])

    return data

def save_data_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Glossary', 'Difference'])
        writer.writerows(data)

html_path = 'downloaded_pages/thesaurus.html'
data = get_data_from_html(html_path)
save_data_to_csv(data)