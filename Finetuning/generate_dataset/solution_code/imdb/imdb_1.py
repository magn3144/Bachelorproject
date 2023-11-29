import requests
from lxml import html
import csv

tree = html.parse('downloaded_pages/imdb.html')

movies = tree.xpath('//div[@class="lister-item-content"]/h3[@class="lister-item-header"]/span[@class="lister-item-year text-muted unbold"]')

with open('scraped_data.csv', 'w', newline='') as csvfile:
    fieldnames=['Movie Release Year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for mv in movies:
        writer.writerow({'Movie Release Year': mv.text.strip()})