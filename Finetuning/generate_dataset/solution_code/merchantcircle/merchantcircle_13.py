import csv
from bs4 import BeautifulSoup

def scrape_html(file_path):
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        view_more_links = soup.find_all('a', class_='viewMoreLink')
        
        scraped_data = []
        for link in view_more_links:
            scraped_data.append(link.get_text(strip=True))
        
        return scraped_data

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Text'])
        writer.writerows([[text] for text in data])

file_path = 'downloaded_pages/merchantcircle.html'
scraped_data = scrape_html(file_path)
save_to_csv(scraped_data)