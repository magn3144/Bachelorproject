import csv
from bs4 import BeautifulSoup

def write_csv(data):
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['text', 'link'])
        for row in data:
            writer.writerow(row)

def scrape_html(file):
    data = []
    with open(file, 'r') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
        h3_elements = soup.find_all('h3', class_='ipc-title__text')
        for h3 in h3_elements:
            a_tag = h3.find('a')
            if a_tag is not None:
                text = a_tag.text
                link = a_tag.get('href', '')
                data.append([text, link])
    return data

def main():
    html_file = 'downloaded_pages/imdb.html'
    scraped_data = scrape_html(html_file)
    write_csv(scraped_data)

if __name__ == "__main__":
    main()