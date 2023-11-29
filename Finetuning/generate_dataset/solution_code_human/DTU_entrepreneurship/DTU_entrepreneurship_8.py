import csv
from lxml import html
import os

def extract_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        page_content = file.read()
    tree = html.fromstring(page_content)
    description_xpath = '//*[@id="footerAbout"]/div[1]'
    description = tree.xpath(description_xpath + '/p/text()')
    if len(description) > 0:
        return description[0].strip()
    return ""

data = []
html_path = "downloaded_pages/DTU_entrepreneurship.html"
description = extract_data(html_path)
data.append([description])
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)