import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/espn.html'
extracted_data = []

with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    player_names = soup.find_all(class_='Athlete__PlayerName')
    for name in player_names:
        extracted_data.append(name.text)

with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Player Name'])
    writer.writerows([[name] for name in extracted_data])