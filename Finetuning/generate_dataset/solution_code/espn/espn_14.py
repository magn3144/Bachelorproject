import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/espn.html'
target_elements = ['div.MediaList__item__description', 'div.News__Item__Description']

scraped_data = []

with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    for element in target_elements:
        elements = soup.select(element)
        for el in elements:
            scraped_data.append(el.get_text())

with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Description'])
    writer.writerows([[data] for data in scraped_data])