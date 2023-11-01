import csv
import re
from lxml import etree


def extract_text(element):
    return element.text.strip() if element is not None and element.text else ''


def scrape_html(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()

    parser = etree.HTMLParser()
    tree = etree.fromstring(html_content, parser)

    population_element = tree.xpath("/html/body/div[1]/main/div/div[2]/div[1]/div/div/div[4]/div/div/div[2]/div/div[1]/p")[0]
    population_text = extract_text(population_element)

    population_size_match = re.search(r'(\d+(?:,\d+)?)', population_text)
    population_size = population_size_match.group(0) if population_size_match else ''

    population_composition_element = tree.xpath("/html/body/div[1]/main/div/div[2]/div[1]/div/div/div[3]/a[3]/div/div[1]/div[3]")[0]
    population_composition = extract_text(population_composition_element)

    population_demographic_element = tree.xpath("/html/body/div[1]/main/div/div[2]/div[1]/div/div/div[1]/div/a/div/div[3]")[0]
    population_demographic = extract_text(population_demographic_element)

    scraped_data = [['Population Size', population_size],
                    ['Population Composition', population_composition],
                    ['Population Demographic', population_demographic]]

    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(scraped_data)


scrape_html('downloaded_pages/dst.html')