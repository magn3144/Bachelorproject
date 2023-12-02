import csv
from lxml import html
from bs4 import BeautifulSoup

with open("downloaded_pages/imdb.html", 'r') as file:
    page_content = file.read()

soup = BeautifulSoup(page_content, 'html.parser')
h3_tags = soup.find_all('h3', {'class': 'ipc-title__text'})

data = []
for tag in h3_tags:
    link = tag.find('a')
    if link is not None:
        data.append({'Text': tag.text.strip(), 'Link': link.get('href')})

with open('scraped_data.csv', 'w') as csvfile:
    fieldnames = ['Text', 'Link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)