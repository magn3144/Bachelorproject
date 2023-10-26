import csv
import requests
from lxml import html


def scrape_page(url, xpaths):
    response = requests.get(url)
    tree = html.fromstring(response.content)

    scraped_data = []
    for xpath in xpaths:
        elements = tree.xpath(xpath)
        for element in elements:
            data = element.text.strip()
            scraped_data.append(data)

    return scraped_data


def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Data'])
        writer.writerows(data)


if __name__ == '__main__':
    xpaths = [
        '/html/body/div/div[2]/div[2]/div[2]/div/section[2]/div/div[1]/article/div/header/h2/a',
        '/html/body/div/div[2]/div[2]/div[2]/div/section[2]/div/div[2]/article/div/header/h2/a',
        '/html/body/div/div[2]/div[2]/div[2]/div/section[2]/div/div[3]/article/div/header/h2/a',
        '/html/body/div/div[2]/div[2]/div[2]/div/section[2]/div/div[4]/article/div/header/h2/a'
    ]

    url = 'file:///path/to/downloaded_pages/foxnews.html'
    scraped_data = scrape_page(url, xpaths)
    save_to_csv(scraped_data)