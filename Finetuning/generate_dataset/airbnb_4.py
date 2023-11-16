import csv
from bs4 import BeautifulSoup

file = open('downloaded_pages/airbnb.html','r')
soup = BeautifulSoup(file, 'html.parser')

location_elems = soup.select('div[id^="title_"]')
price_elems = soup.select('span.a8jt5op')
data = []

for location, price in zip(location_elems, price_elems):
    location_text = location.get_text(strip=True)
    price_text = price.get_text(strip=True)
    data.append([location_text, price_text])

with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Location", "Price"])
    writer.writerows(data)