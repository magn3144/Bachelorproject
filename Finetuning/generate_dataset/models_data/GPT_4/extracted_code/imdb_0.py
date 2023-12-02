import csv
from bs4 import BeautifulSoup

def parse():
    soup = BeautifulSoup(open('downloaded_pages/imdb.html'), 'html.parser')
    movies = []

    for title in soup.find_all('h3', class_='ipc-title__text'):
        name = title.text.strip()
        movies.append(name)
    
    with open('scraped_data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Title"])
        for title in movies:
            writer.writerow([title])

if __name__ == '__main__':
    parse()