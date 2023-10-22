import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/washingtonpost.html'
target_elements = ['<p class="wpds-c-kjCVnC">', '</p>']

with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    p_tags = soup.find_all('p', class_='wpds-c-kjCVnC')

    data = []
    for tag in p_tags:
        text = tag.get_text(strip=True)
        data.append(text)

    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Scraped Data'])
        writer.writerows([[d] for d in data])