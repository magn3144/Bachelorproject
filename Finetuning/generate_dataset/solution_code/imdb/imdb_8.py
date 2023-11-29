import csv
from bs4 import BeautifulSoup

with open("downloaded_pages/imdb.html", 'r') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'lxml')

footer_links = soup.find_all('a', {'class': 'ipc-link ipc-link--baseAlt ipc-link--touch-target ipc-link--inherit-color'})

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for link in footer_links:
        writer.writerow([link.get_text(), link['href']])