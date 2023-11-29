import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_social_links():
    driver = webdriver.Firefox(executable_path='/path/to/geckodriver')
    driver.get('file:///path/to/downloaded_pages/imdb.html')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    socials_div = soup.find_all('div', class_='ipc-page-content-container ipc-page-content-container--center')[1]
    links = socials_div.find_all('a')
    social_links = [link['href'] for link in links if 'facebook' in link['href'] or 'instagram' in link['href'] or 'twitter' in link['href']]

    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Social Links'])
        for link in social_links:
            writer.writerow([link])

    driver.quit()

get_social_links()