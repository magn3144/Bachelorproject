from bs4 import BeautifulSoup
import csv
import os

with open(os.path.join('downloaded_pages', 'imdb.html'), 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    news_titles = soup.find_all('div', class_='sc-bb1bba6c-1 ipcpFw news-preview-card-articleTitle')

data = []
for title in news_titles:
    data.append([title.text.strip()])

with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in data:
        writer.writerow(row)