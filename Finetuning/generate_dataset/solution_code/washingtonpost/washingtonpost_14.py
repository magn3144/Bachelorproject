import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/washingtonpost.html'
output_file = 'scraped_data.csv'

with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    p_tags = soup.find_all('p', class_='wpds-c-kjCVnC')

    data = []
    for p_tag in p_tags:
        data.append(p_tag.text.strip())

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)