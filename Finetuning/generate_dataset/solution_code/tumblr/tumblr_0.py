from bs4 import BeautifulSoup
import csv

def scrape_page(local_path):
    with open(local_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    titles = soup.find_all('h1', class_='hF8Wr YkQj_')
    
    data = []
    for title in titles:
        data.append(title.text)
    
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title'])
        for title in data:
            writer.writerow([title])

scrape_page('downloaded_pages/tumblr.html')