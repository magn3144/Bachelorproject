import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/washingtonpost.html'

def scrape_links(html_file):
    with open(html_file) as file:
        soup = BeautifulSoup(file, 'html.parser')
    links = soup.find_all('a')
    data = []
    for link in links:
        if link.get('href'):
            data.append({'Link': link.get('href')})
    return data

data = scrape_links(html_file)

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Link'])
    writer.writeheader()
    writer.writerows(data)