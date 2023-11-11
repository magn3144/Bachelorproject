import csv
from lxml import etree

def extract_movies_positions(html_file):
    tree = etree.parse(html_file)
    movies = tree.xpath("/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[position()>=55 and position()<=66]/div[2]/div/div/div[1]/a/h3")
    positions = [movie.text.split(". ")[0] for movie in movies]
    titles = [movie.text.split(". ")[1] for movie in movies]
    return list(zip(positions, titles))

def save_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Position', 'Title'])
        writer.writerows(data)

html_file = 'downloaded_pages/imdb.html'
movies_positions = extract_movies_positions(html_file)
save_csv(movies_positions)