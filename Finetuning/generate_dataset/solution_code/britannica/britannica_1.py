from typing import Dict, List
import csv
from lxml import etree

def get_elements_from_html(file_path: str, category: str, elements: Dict[str, str]) -> List[str]:
    with open(file_path, 'r') as file:
        html = file.read()

    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)

    scraped_data = []

    for key, xpath in elements.items():
        elements = tree.xpath(xpath)
        for element in elements:
            scraped_data.append(element.text)

    return scraped_data


def save_to_csv(data: List[str]):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Login Text'])
        for item in data:
            writer.writerow([item])


file_path = 'downloaded_pages/britannica.html'
category = 'Educational Websites'

elements = {
    'Login Text': '/html/body/header/div[1]/div/div[2]/button/span'
}

scraped_data = get_elements_from_html(file_path, category, elements)
save_to_csv(scraped_data)