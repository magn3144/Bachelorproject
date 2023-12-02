import csv
import os
from bs4 import BeautifulSoup

html_file = open('downloaded_pages/imdb.html', 'r')
soup = BeautifulSoup(html_file, 'html.parser')
html_file.close()

table = soup.find_all('div', {'class': 'lister-item-content'})
movie_duration = []

for movie in table:
    try:
        duration = movie.find('span', {'class': 'runtime'}).text
    except AttributeError:
        duration = "N/A"
    movie_duration.append([duration])

with open('scraped_data.csv', 'w', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(movie_duration)