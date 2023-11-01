import csv
import re

from lxml import etree

def get_percentage(element_text):
    percentage = re.search(r'\d+%', element_text)
    return percentage.group(0) if percentage else ""

def scrape_data():
    html_file_path = "downloaded_pages/y8.html"

    with open(html_file_path, "rb") as file:
        html = file.read()

    tree = etree.HTML(html)

    elements = [
        '/html/body/div[1]/div[5]/div[2]/ul/li[11]/a/div[2]/div[3]',
        '/html/body/div[1]/div[5]/div[2]/ul/li[8]/a/div[2]/div[2]/span',
        '/html/body/div[1]/div[5]/div[2]/ul/li[16]/a/div[2]/div[3]',
        '/html/body/div[1]/div[5]/div[2]/ul/li[28]/a/div[2]/div[2]/span',
        '/html/body/div[1]/div[5]/div[2]/ul/li[24]/a/span',
        '/html/body/div[1]/div[5]/div[2]/ul/li[4]/a/div[2]/div[3]',
        '/html/body/div[1]/div[5]/div[2]/ul/li[50]/a/div[2]/div[3]'
    ]

    data = []
    for element in elements:
        element_text = tree.xpath(element + '/text()')
        percentage = get_percentage(element_text[0].strip()) if element_text else ""
        data.append(percentage)

    with open("scraped_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Percentage"])
        writer.writerows(zip(data))