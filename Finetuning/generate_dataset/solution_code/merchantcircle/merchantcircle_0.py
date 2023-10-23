import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/merchantcircle.html'

with open(html_file) as file:
    soup = BeautifulSoup(file, 'html.parser')
    spans = soup.find_all('span', class_='fullText')

data = []
for span in spans:
    data.append(span.get_text())

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Full Text'])
    writer.writerows(zip(data))