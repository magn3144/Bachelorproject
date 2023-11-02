import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/espn.html'

def parse_html(html_file):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
    return soup

def extract_inactives(soup):
    inactives = ""
    for div in soup.find_all('div', class_='News__Item__Description'):
        inactives = div.text.strip()
    return inactives

def extract_analysis(soup):
    analysis = ""
    for p in soup.find_all('p', class_='n9 clr-gray-03'):
        analysis = p.text.strip()
    return analysis

def save_to_csv(data):
    headers = ['Inactives', 'Analysis']
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow(data)

soup = parse_html(html_file)
inactives = extract_inactives(soup)
analysis = extract_analysis(soup)
data = [inactives, analysis]
save_to_csv(data)