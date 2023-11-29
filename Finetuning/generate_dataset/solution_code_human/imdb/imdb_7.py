from bs4 import BeautifulSoup
import csv
import os

def get_social_links(filepath):
    with open(filepath, 'r') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
    footer = soup.find('footer')
    social_links = footer.find_all('a', {'class': 'ipc-icon-link ipc-icon-link--baseAlt ipc-icon-link--onBase'})

    data = []
    for link in social_links:
        href = link.get('href')
        if "http" in href:
            data.append({ "social_link": href })
            
    keys = data[0].keys()

    with open('scraped_data.csv', 'w', newline='')  as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

filepath = os.path.join("downloaded_pages", "imdb.html")
get_social_links(filepath)