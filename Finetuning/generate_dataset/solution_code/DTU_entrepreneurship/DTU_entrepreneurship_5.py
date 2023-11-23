import csv
from bs4 import BeautifulSoup
import os


html_file_path = os.path.join('downloaded_pages', 'DTU_entrepreneurship.html')

with open(html_file_path, 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

    links = soup.find_all('a')

    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Link Text', 'Link URL'])

        for link in links:
            link_text = link.text
            link_text = link_text.replace(',', '').replace('\n', '')
            link_url = link.get('href')
            if link_text and link_url:
                writer.writerow([link_text, link_url])