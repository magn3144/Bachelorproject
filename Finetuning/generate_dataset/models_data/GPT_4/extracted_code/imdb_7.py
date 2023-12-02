from bs4 import BeautifulSoup
import csv
import os

file_path = 'downloaded_pages/imdb.html'

with open(file_path, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

social_links = soup.find_all('a', {'class': 'ipc-icon-link ipc-icon-link--baseAlt ipc-icon-link--onBase'})
links = [link['href'] for link in social_links]

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Social Links"])
    for link in links:
        writer.writerow([link])