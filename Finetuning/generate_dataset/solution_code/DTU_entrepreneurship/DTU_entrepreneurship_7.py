import csv
from bs4 import BeautifulSoup

with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

h2_headings = soup.find_all('h2', class_="a-heading-h1 o-hero__title")

data = []

for h2 in h2_headings:
    data.append(h2.text)

with open('scraped_data.csv', 'w') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow([row])