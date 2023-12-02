import csv
from lxml import etree
from bs4 import BeautifulSoup

path_to_html_file = "downloaded_pages/imdb.html"
with open(path_to_html_file, 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'lxml')

ratings = []
for i in range(1, 251):
    xpath_to_rating = f"/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[{i}]/div[2]/div/div/span/div/span/span"
    element = soup.xpath(xpath_to_rating)
    if element:
        ratings.append(element[0].text.strip())

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Rating"])
    for rating in ratings:
        writer.writerow([rating])