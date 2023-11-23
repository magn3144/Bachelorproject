import requests
from bs4 import BeautifulSoup
import csv

def write_to_csv(data):
    with open('scraped_data.csv', mode='w') as file:
        writer = csv.writer(file)
        for url in data:
            writer.writerow([url])

def extract_social_links(page_path):
    with open(page_path, 'r', encoding='utf8') as file:
        page_content = file.read()
    soup = BeautifulSoup(page_content, 'lxml')
    social_links = []

    for link in soup.find_all('a', href=True):
        if "facebook.com" in link['href'] or "instagram.com" in link['href'] or \
           "linkedin.com" in link['href'] or "twitter.com" in link['href'] or "youtube.com" in link['href']:
            social_links.append(link['href'].replace('\n', ''))
    
    return social_links


social_links = extract_social_links("downloaded_pages/DTU_entrepreneurship.html")
write_to_csv(social_links)