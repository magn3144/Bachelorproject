import csv
from lxml import html
from bs4 import BeautifulSoup

with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as file:
    page_content = file.read()

soup = BeautifulSoup(page_content, 'html.parser')
social_links = soup.find_all('a', attrs={'class': 'social-media-icon'})

with open('scraped_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Socials Links"])
    for link in social_links:
        writer.writerow([link['href']])