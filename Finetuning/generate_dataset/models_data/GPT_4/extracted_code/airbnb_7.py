import requests
from bs4 import BeautifulSoup
import pandas as pd

with open('downloaded_pages/airbnb.html', 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'lxml')

data = []
header_menu = soup.find_all(class_='l1ovpqvx c1kblhex dir dir-ltr')

for item in header_menu:
    data.append(item.text)

df = pd.DataFrame(data, columns=['Airbnb Types'])

df.to_csv('scraped_data.csv', index=False)