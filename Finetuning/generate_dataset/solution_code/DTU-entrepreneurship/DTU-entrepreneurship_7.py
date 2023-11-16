import csv
import re
from bs4 import BeautifulSoup

def parse_html(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    return soup

def extract_dates(soup):
    date_pattern = re.compile(r'\b(\d{1,2}\s[A-Z][a-z]+\s\d{4})\b')
    dates = []
    for tag in soup.find_all(text=date_pattern):
        match = date_pattern.search(tag)
        if match: 
            dates.append(match.group())
    return dates

def write_to_csv(dates, file_path='scraped_data.csv'):
    with open(file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Dates'])
        for date in dates:
            writer.writerow([date])

soup = parse_html('downloaded_pages/DTU-entrepreneurship.html')
dates = extract_dates(soup)
write_to_csv(dates)