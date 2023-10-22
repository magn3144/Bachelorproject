import csv
from bs4 import BeautifulSoup

html_file = "downloaded_pages/merchantcircle.html"

def scrape_street_addresses(html_file):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        street_addresses = soup.find_all('span', class_='street-address')
        addresses = [addr.getText().strip() for addr in street_addresses]
        return addresses

data = scrape_street_addresses(html_file)

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Street Address"])
    for address in data:
        writer.writerow([address])