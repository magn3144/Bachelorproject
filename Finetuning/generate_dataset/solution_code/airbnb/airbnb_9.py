import csv
from bs4 import BeautifulSoup

def is_guest_favorite(soup, xpath):
    try:
        div = soup.find('div', {'class': 't1qa5xaj dir dir-ltr'})
        path_parts = xpath.split('/')
        for part in path_parts[2:]:
            if '[' in part and ']' in part:
                index = int(part.split('[')[1].split(']')[0]) - 1
                div = div.contents[index]
            else:
                div = getattr(div, part)
        if div.text == 'Guest favorite':
            return 'yes'
    except:
        pass
    return 'no'

def extract_data(soup, xpath):
    try:
        tag = soup.html
        path_parts = xpath.split('/')
        for part in path_parts[2:]:
            if '[' in part and ']' in part:
                index = int(part.split('[')[1].split(']')[0]) - 1
                tag = tag.contents[index]
            else:
                tag = getattr(tag, part)
        return tag.text
    except:
        return ''

html_file = 'downloaded_pages/airbnb.html'
with open(html_file, 'r') as file:
    data = file.read()

soup = BeautifulSoup(data, 'html.parser')

airbnb_data = []
xpaths = [
    '/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[35]/div/div[2]/div/div/div/div/div/div[2]/div[1]',
    '/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[13]/div/div[2]/div/div/div/div/div/div[2]/div[1]',
]

for path in xpaths:
    location = extract_data(soup, path)
    favorite = is_guest_favorite(soup, path)
    airbnb_data.append((location, favorite))

with open('scraped_data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(airbnb_data)