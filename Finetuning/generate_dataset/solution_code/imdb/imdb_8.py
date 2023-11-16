import csv
from lxml import html
from bs4 import BeautifulSoup

with open('downloaded_pages/imdb.html', 'r') as file:
    soup = BeautifulSoup(file, 'lxml')

footer = soup.find('footer')
links = footer.find_all('a')
with open('scraped_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Text', 'Link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for link in links:
        writer.writerow({'Text': link.text, 'Link': link.get('href')})