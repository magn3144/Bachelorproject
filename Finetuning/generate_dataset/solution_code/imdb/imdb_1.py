import csv
from bs4 import BeautifulSoup

def scrape_imdb_top250(html_path):
    with open(html_path, 'r') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'lxml')

    top250 = soup.select('div.ul > li')

    movie_rankings = []

    for movie in top250:
        rank = movie.h3.contents[0].strip().split('.')[0]
        movie_rankings.append(rank)

    return movie_rankings

file_path = "downloaded_pages/imdb.html"
rankings = scrape_imdb_top250(file_path)

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for rank in rankings:
       writer.writerow([rank])