import csv
from bs4 import BeautifulSoup

path = 'downloaded_pages/fbi.html'

def extract_data():
    with open(path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        section = soup.find('div', class_='legal-policies-disclaimers')
        links = section.find_all('a')

        data = []
        for link in links:
            name = link.text
            href = link.get('href')
            data.append([name, href])

    return data

def save_data(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Link'])
        writer.writerows(data)

if __name__ == '__main__':
    scraped_data = extract_data()
    save_data(scraped_data)