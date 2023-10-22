import csv
from bs4 import BeautifulSoup

def extract_journalists(html_file):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        journalist_names = []
        for element in soup.find_all(['a', 'span']):
            if element.text.strip() and element.text.strip().istitle():
                journalist_names.append(element.text.strip())
    return journalist_names

def save_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Journalist Name'])
        writer.writerows(data)

html_path = 'downloaded_pages/washingtonpost.html'
journalists = extract_journalists(html_path)
save_csv(journalists, 'scraped_data.csv')