import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/census.html'
target_data = []

with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    fact_sheet_titles = soup.find_all('a', class_='uscb-header-panel-content-link')

    for title in fact_sheet_titles:
        target_data.append(title.get_text().strip())

with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Fact Sheet Titles"])
    writer.writerows(zip(target_data))