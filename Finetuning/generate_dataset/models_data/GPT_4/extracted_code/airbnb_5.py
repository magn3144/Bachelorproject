import csv
from lxml import etree
from bs4 import BeautifulSoup


def main():
    with open('downloaded_pages/airbnb.html', 'r') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    airbnbs = soup.find_all('div', class_='t1jojoys dir dir-ltr')
    links = soup.find_all('a', class_='l1ovpqvx c1kblhex dir dir-ltr')

    data = []

    for airbnb, link in zip(airbnbs, links):
        data.append({
            'Location': airbnb.get_text(),
            'Link': link.get('href')
        })

    with open('scraped_data.csv', 'w') as csv_file:
        fieldnames = ['Location', 'Link']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    main()