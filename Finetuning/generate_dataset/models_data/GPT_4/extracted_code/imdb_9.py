import csv
from bs4 import BeautifulSoup

html_file_path = 'downloaded_pages/imdb.html'
with open(html_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'lxml')
title = soup.find('h1', class_='ipc-title__text chart-layout-specific-title-text').text

with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([title])