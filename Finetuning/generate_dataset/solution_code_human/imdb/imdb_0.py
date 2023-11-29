import csv
from lxml import html
from typing import List

def parse(file_path: str) -> List[str]:
    parser = html.HTMLParser(encoding='utf-8')
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = html.parse(file, parser=parser)
    titles = tree.xpath('//h3[@class="ipc-title__text"]/text()')
    # Remove titles not starting with a number
    titles = [title for title in titles if title[0].isdigit()]

    return titles

def write_to_csv(data: List[str], file_name: str = 'scraped_data.csv') -> None:
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow([item])


file_path = 'downloaded_pages/imdb.html'
parsed_data = parse(file_path)
write_to_csv(parsed_data)