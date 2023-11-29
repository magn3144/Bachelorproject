import csv
from lxml import html

with open('downloaded_pages/imdb.html', 'r') as file:
    page_content = file.read()

tree = html.fromstring(page_content)

title = tree.xpath('/html/body/div[2]/main/div/div[3]/section/div/div[1]/div/div[2]/hgroup/h1/text()')[0]

with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([title])