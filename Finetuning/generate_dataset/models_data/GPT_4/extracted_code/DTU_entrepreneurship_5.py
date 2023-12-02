import csv
import bs4
import os

def get_links(soup):
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None:
            links.append(href)
    return links

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def main():
    with open(os.path.join('downloaded_pages', 'DTU_entrepreneurship.html'), 'r') as html_file:
        soup = bs4.BeautifulSoup(html_file, 'html.parser')
    links = get_links(soup)
    save_to_csv(links)

if __name__ == '__main__':
    main()