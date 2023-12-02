

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_html_text(url):
    r = requests.get(url)
    return r.text

def get_location_and_price(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    location = soup.find('span', class_='u17llcap dir dir-ltr').text
    price = soup.find('span', class_='a8jt5op dir dir-ltr').text
    return location, price

def get_all_location_and_price(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    location_and_price = []
    for location in soup.find_all('span', class_='u17llcap dir dir-ltr'):
        for price in soup.find_all('span', class_='a8jt5op dir dir-ltr'):
            location_and_price.append([location.text, price.text])
    return location_and_price

def get_all_location_and_price_from_url(url):
    html_text = get_html_text(url)
    return get_all_location_and_price(html_text)

def save_to_csv(location_and_price):
    df = pd.DataFrame(location_and_price, columns=['Location', 'Price'])
    df.to_csv('scraped_data.csv', index=False)

def main():
    url = 'https://www.airbnb.com/s/New-York--NY--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=december&flexible_trip_dates%5B%5D=january&flexible_trip_dates%5B%5D=february&date_picker_type=flexible_dates&source=structured_search_input_header&search_type=search_query&checkin=2020-12-21&checkout=2020-12-28&price_min=100&price_max=1000&room_type=Entire%20home%2Fapt'
    location_and_price = get_all_location_and_price_from_url(url)
    save_to_csv(location_and_price)

if __name__ == '__main__':
    main()

