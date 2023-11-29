import csv
from lxml import html
import os

file_path = os.path.join("downloaded_pages", "imdb.html")

with open(file_path, "r") as file:
    content = file.read()

parsed_html = html.fromstring(content)

data = []
for i in range(1, 251):
    movie_name_path = f"/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[{i}]/div[2]/div/div/div[1]/a/h3"
    movie_ratings_path = f"/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[{i}]/div[2]/div/div/span/div/span/span"

    movie_name = parsed_html.xpath(movie_name_path)
    movie_ratings = parsed_html.xpath(movie_ratings_path)

    if movie_name and movie_ratings:
        movie_name = movie_name[0].text_content()
        movie_ratings = movie_ratings[0].text_content().replace("(", "").replace(")", "").replace("K", "000")

        data.append({
            "Movie": movie_name,
            "Ratings": movie_ratings
        })

with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Movie", "Ratings"])
    writer.writeheader()
    writer.writerows(data)