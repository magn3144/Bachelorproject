import csv
import requests
from lxml import html

def scrape_department_links(path):
    with open(path, 'r') as file:
        page_content = file.read()

    tree = html.fromstring(page_content)

    department_headers = tree.xpath('//h2[text()="Departments and Centres"]')

    departments = []

    for header in department_headers:
        div = header.getparent()
        links = div.xpath('.//a')

        for link in links:
            name = link.text_content()
            departments.append({'name': name})

    with open('scraped_data.csv', 'w', newline='') as file:
        fieldnames = ['name']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(departments)

scrape_department_links('downloaded_pages/DTU_entrepreneurship.html')