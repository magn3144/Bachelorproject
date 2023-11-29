import csv
from bs4 import BeautifulSoup

with open("downloaded_pages/DTU_entrepreneurship.html", 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    address_div = soup.find('div', {'class': 'footeraddresstitle grid_5 alpha'}).text.strip().replace('"', '')
    with open("scraped_data.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([f'"{address_div}"'])