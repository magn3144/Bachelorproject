import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/merchantcircle.html'
target_elements = ['inMob']

def scrape_target_data(html_file, target_elements):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        scraped_data = []
        for element in target_elements:
            spans = soup.find_all('span', class_=element)
            for span in spans:
                scraped_data.append(span.text.strip())
    
    return scraped_data

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

data = scrape_target_data(html_file, target_elements)
save_to_csv(data)