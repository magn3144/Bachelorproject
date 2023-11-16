import re
import csv
from lxml import html


def get_identifiers(page_content):
    identifiers = re.findall(r'[0-9]{6,}', page_content)
    return identifiers

def save_to_file(data):
    with open('scraped_data.csv', 'w') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow([row])

def scrape_file(file_path):
    with open(file_path, 'r') as f:
        page_content = f.read()

    identifiers = get_identifiers(page_content)
    save_to_file(identifiers)


scrape_file('downloaded_pages/DTU-entrepreneurship.html')