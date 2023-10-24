import csv
from bs4 import BeautifulSoup

html_path = 'downloaded_pages/ppubs.html'

def extract_hyperlinks(html_path):
    with open(html_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        links = soup.find_all('a')
        data = []

        for link in links:
            text = link.get_text(strip=True)
            href = link.get('href')
            data.append([text, href])

    return data

data = extract_hyperlinks(html_path)

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)