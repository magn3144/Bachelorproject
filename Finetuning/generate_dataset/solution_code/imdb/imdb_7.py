import csv
from lxml import etree

html_path = 'downloaded_pages/imdb.html'
csv_path = 'scraped_data.csv'

with open(html_path, 'r') as f:
    html_string = f.read()

parser = etree.HTMLParser()
tree = etree.fromstring(html_string, parser)

ranks = [element.text for element in tree.xpath('//div[@class="ipc-simple-select__selected-option"]')]
titles = [element.text for element in tree.xpath('//h3[@class="ipc-title__text"]')]
ratings = [element.text for element in tree.xpath('//span[@class="ipc-rating-star--voteCount"]')]

movies = list(zip(ranks, titles, ratings))

with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Rank", "Title", "Rating"])
    writer.writerows(movies)