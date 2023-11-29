import csv
from lxml import etree
from bs4 import BeautifulSoup

def scrape_headings(file_path):
    with open(file_path, 'r') as file:
        html_text = file.read()

    soup = BeautifulSoup(html_text, 'lxml')
    headings = [heading.text for heading in soup.find_all('h2')]

    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for heading in headings:
            writer.writerow([heading])

scrape_headings('downloaded_pages/DTU_entrepreneurship.html')