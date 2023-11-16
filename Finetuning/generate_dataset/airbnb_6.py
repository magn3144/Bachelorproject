from bs4 import BeautifulSoup
import csv
import os

def extract_data(file):
    with open(file, 'r', encoding='utf-8') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
    section = soup.find_all('h2', {'class': 'hifxi0b dir dir-ltr'})
    for sec in section:
        if sec.text == 'Inspiration for future getaways':
            target_div = sec.find_parent('div')
            locations = target_div.find_all('div', {'class': 't1jojoys dir dir-ltr'})
            records = []
            for location in locations:
                text = location.text
                link = location.find_previous_sibling('a')['href']
                records.append((text, link))

    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Location Name', 'Location Link'])
        writer.writerows(records)


if __name__ == "__main__":
    file_path = os.path.join('downloaded_pages', 'airbnb.html')
    extract_data(file_path)