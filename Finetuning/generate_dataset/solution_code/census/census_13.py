import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/census.html'

soup = BeautifulSoup(open(html_file), 'html.parser')

target_elements = soup.find_all('div', class_='uscb-default-x-column-content uscb-body-small-01')

data = []
for element in target_elements:
    if 'all personally id' in element.text:
        data.append(element.text.strip())

with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Scraped Data'])
    for row in data:
        writer.writerow([row])