import csv
from lxml import html
import re

with open("downloaded_pages/imdb.html", "r") as file:
    page = file.read()
tree = html.fromstring(page)

rows = []
for i in range(1, 250):
    xpath_title = f'/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[{i}]/div[2]/div/div/div[1]/a/h3'
    xpath_user_rating = f'/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[{i}]/div[2]/div/div/span/div/span/span'
    title = tree.xpath(xpath_title)
    user_rating = tree.xpath(xpath_user_rating)
    if title and user_rating:
        rows.append({"title": title[0].text, "user_rating": re.findall(r'\d+', user_rating[0].text)[0]})
        
with open('scraped_data.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'user_rating'])
    writer.writeheader()
    for row in rows:
        writer.writerow(row)