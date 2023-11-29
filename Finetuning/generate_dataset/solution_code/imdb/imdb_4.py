import csv
import requests
from lxml import html

csv_filename = 'scraped_data.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['Movie Title', 'Age Rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    path_to_html_file = 'downloaded_pages/imdb.html'
    with open(path_to_html_file, 'r') as f:
        page_content = f.read()

    tree = html.fromstring(page_content)
    for i in range(1, 251):
        movie_title = tree.xpath(f'/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[{i}]/div[2]/div/div/div[1]/a/h3/text()')
        age_rating = tree.xpath(f'/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[{i}]/div[2]/div/div/div[2]/span[3]/text()')
        
        if movie_title and age_rating:
            writer.writerow({'Movie Title': movie_title[0], 'Age Rating': age_rating[0]})
