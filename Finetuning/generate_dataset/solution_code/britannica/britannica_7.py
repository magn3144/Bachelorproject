import os
import csv
from lxml import etree


def extract_titles(html_path, xpaths):
    tree = etree.parse(html_path)
    titles = []
    for xpath in xpaths:
        element = tree.xpath(xpath)[0]
        title = element.text.strip()
        titles.append(title)
    return titles


def save_csv(data):
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title'])
        writer.writerows([[title] for title in data])


def main():
    category = 'Educational Websites'
    web_page = 'britannica'
    html_path = f'downloaded_pages/{web_page}.html'
    xpaths = [
        '/html/body/main/div/div/div/div[7]/div[2]/div/p',
        '/html/body/main/div/div/div/div[7]/div[5]/div/p',
        '/html/body/main/div/div/div/div[7]/div[1]/div/p',
    ]

    titles = extract_titles(html_path, xpaths)
    save_csv(titles)


if __name__ == '__main__':
    main()