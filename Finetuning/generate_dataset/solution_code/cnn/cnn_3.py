import csv
from bs4 import BeautifulSoup


def get_html_elements(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.find_all('label', class_='ad-feedback__emoji-base')


def get_label(element):
    return element.get('class')[1].replace('ad-feedback__emoji-', '')


def scrape_data():
    html_file = 'downloaded_pages/cnn.html'
    elements = get_html_elements(html_file)
    
    data = []
    for element in elements:
        label = get_label(element)
        data.append(label)

    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Labels'])
        writer.writerows(data)


if __name__ == '__main__':
    scrape_data()