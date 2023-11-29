from bs4 import BeautifulSoup
import csv
import re

html_file = open('downloaded_pages/imdb.html', 'r')
soup = BeautifulSoup(html_file, 'html.parser')

csv_data = [['Release Year']]
# Find all the spans with class 'sc-479faa3c-8 bNrEFi cli-title-metadata-item'
for movie_meta in soup.find_all('span', class_='sc-479faa3c-8 bNrEFi cli-title-metadata-item'):
    year_text = movie_meta.text
    if re.search(r'\d{4}', year_text):
        year = re.search(r'\d{4}', year_text).group()
        csv_data.append([year])

with open("scraped_data.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_data)