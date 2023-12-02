import csv
from bs4 import BeautifulSoup

def scrape_show_more_button_class():
    soup = BeautifulSoup(open('downloaded_pages/airbnb.html'), 'html.parser')
    show_more_button = soup.find_all('button', string='Show more')
    
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for button in show_more_button:
            writer.writerow([button.get('class')])

scrape_show_more_button_class()