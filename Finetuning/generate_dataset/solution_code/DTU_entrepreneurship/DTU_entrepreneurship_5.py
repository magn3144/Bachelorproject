import csv
from lxml import html
from bs4 import BeautifulSoup

html_content = ''
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "lxml")
links = soup.find_all('a')
absolute_links = ['http://www.dtu.dk' + link.get('href') if link.get('href').startswith('/') else link.get('href') for link in links if link.get('href') != None]

with open('scraped_data.csv', 'w') as file:
    writer = csv.writer(file)
    [writer.writerow([link]) for link in absolute_links]