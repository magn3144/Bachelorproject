import csv
from lxml import html
from typing import List

def parse(file_path: str) -> List[str]:
    parser = html.HTMLParser(encoding='utf-8')
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = html.parse(file, parser=parser)
    titles = tree.xpath('//h3[@class="ipc-title__text"]/text()')
    return titles

def write_to_csv(data: List[str], file_name: str = 'scraped_data.csv') -> None:
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow([item])

if __name__ == '__main__':
    file_path = 'downloaded_pages/imdb.html'
    parsed_data = parse(file_path)
    write_to_csv(parsed_data)