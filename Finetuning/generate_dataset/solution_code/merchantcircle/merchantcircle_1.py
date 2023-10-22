import csv
from bs4 import BeautifulSoup

def scrape_sub_menu_headers(html_file):
    with open(html_file, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        sub_menu_headers = soup.find_all('li', class_='sub-menu-header')

    data = []
    for header in sub_menu_headers:
        data.append(header.text.strip())

    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Sub Menu Headers'])
        writer.writerows(data)

scrape_sub_menu_headers('downloaded_pages/merchantcircle.html')