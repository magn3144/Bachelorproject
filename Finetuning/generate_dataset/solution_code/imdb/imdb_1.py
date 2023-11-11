import csv
from bs4 import BeautifulSoup

def get_text_from_xpath(soup, xpath):
    elements = soup.xpath(xpath)
    return [element.get_text() for element in elements]

def save_data_as_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Rating'])
        for title, rating in data:
            writer.writerow([title, rating])

def main():
    html_file = 'downloaded_pages/imdb.html'
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    titles = get_text_from_xpath(soup, '//h3[@class="ipc-title__text"]')
    ratings = get_text_from_xpath(soup, '//span[@class="ipc-rating-star--rate"]')

    data = list(zip(titles, ratings))
    save_data_as_csv(data)

if __name__ == '__main__':
    main()