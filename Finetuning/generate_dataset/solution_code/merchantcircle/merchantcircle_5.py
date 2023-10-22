import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/merchantcircle.html'

def scrape_html(html_file):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        in_desktop_spans = soup.find_all('span', class_='inDesktop')
        text_list = [span.get_text(strip=True) for span in in_desktop_spans]
        return text_list

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Text'])
        writer.writerows([[text] for text in data])

target_data = scrape_html(html_file)
save_to_csv(target_data)