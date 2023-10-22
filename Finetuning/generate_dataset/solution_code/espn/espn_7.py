import csv
from bs4 import BeautifulSoup

file_path = 'downloaded_pages/espn.html'
target_elements = ['Fantasy football Week 7 inactives:', 'Fantasy football inactives:']
scraped_data = []

with open(file_path, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    
    for element in target_elements:
        data = soup.find('h2', text=element)
        if data:
            inactives = data.find_next('li', class_='MediaList__item__playing')
            if inactives:
                scraped_data.append(inactives.text)

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Fantasy Football Inactives'])
    writer.writerows([[inactive] for inactive in scraped_data])