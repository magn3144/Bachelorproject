import csv
from lxml import html
import os

def parse_file():
    with open("downloaded_pages/imdb.html", "r") as file:
        page = file.read()
    tree = html.fromstring(page)
    movie_list = []
    for i in range(1,251):
        try:
            age_rating = tree.xpath('/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li['+str(i)+']/div[2]/div/div/div[2]/span[3]/text()')[0]
        except:
            age_rating = ''
        movie_title = tree.xpath('/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li['+str(i)+']/div[2]/div/div/div[1]/a/h3/text()')[0]
        movie_list.append([movie_title, age_rating])
    with open('scraped_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(movie_list)

if __name__ == "__main__":
    parse_file()