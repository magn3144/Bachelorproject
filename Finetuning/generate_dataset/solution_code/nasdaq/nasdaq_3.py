import csv
from pathlib import Path
from bs4 import BeautifulSoup


def scrape_span_elements(html):
    soup = BeautifulSoup(html, 'html.parser')
    span_elements = soup.find_all('span', class_='primary-nav__header')
    return span_elements


def save_to_csv(data):
    csv_file = 'scraped_data.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Span Element'])
        for item in data:
            writer.writerow([item.text])


def main():
    local_path = 'downloaded_pages/nasdaq.html'
    with open(local_path, 'r') as file:
        html = file.read()
        span_elements = scrape_span_elements(html)
        save_to_csv(span_elements)


if __name__ == '__main__':
    main()