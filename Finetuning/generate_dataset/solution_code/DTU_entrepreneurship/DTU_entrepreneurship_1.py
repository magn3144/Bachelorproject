import csv
from bs4 import BeautifulSoup
import os

def get_social_links(soup):
    footer = soup.find('footer')
    links = footer.find_all('a')

    social_links = []
    for link in links:
        href = link.get('href')
        if 'facebook.com' in href or 'linkedin.com' in href or 'instagram.com' in href or 'twitter.com' in href:
            social_links.append(href)
    return social_links

def write_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["social_links"])
        for row in data:
            writer.writerow([row])

if __name__ == "__main__":
    filepath = os.path.join('downloaded_pages', 'DTU_entrepreneurship.html')
    with open(filepath, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    social_links = get_social_links(soup)
    
    write_to_csv(social_links)