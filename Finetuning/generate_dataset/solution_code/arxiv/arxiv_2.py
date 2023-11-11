import csv
import pathlib
import re
from lxml import etree

def extract_xpath(html_file_path, xpath):
    with open(html_file_path, 'r') as f:
        html = f.read()
    tree = etree.HTML(html)
    elements = tree.xpath(xpath)
    return elements

def extract_arxiv_ids_and_categories(html_file_path):
    arxiv_id_xpath = '/html/body/div[4]/div/dl/dt/span/a'
    cross_list_category_xpath = '/html/body/div[4]/div/dl/dt/span/a/following-sibling::text()[1]'

    arxiv_ids = extract_xpath(html_file_path, arxiv_id_xpath)
    cross_list_categories = extract_xpath(html_file_path, cross_list_category_xpath)
    data = zip(arxiv_ids, cross_list_categories)

    return data

def save_data_to_csv(data):
    csv_file_path = 'scraped_data.csv'
    with open(csv_file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['arXiv ID', 'Cross-List Category'])
        writer.writerows(data)

html_file_path = 'downloaded_pages/arxiv.html'
data = extract_arxiv_ids_and_categories(html_file_path)
save_data_to_csv(data)