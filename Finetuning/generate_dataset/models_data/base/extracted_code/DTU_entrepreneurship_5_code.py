

import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.dtu.dk/en/entrepreneurship'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

links = []

for link in soup.find_all('a'):
    links.append(link.get('href'))

with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Links'])
    for link in links:
        writer.writerow([link])

