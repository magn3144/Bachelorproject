import csv
from lxml import html
from pathlib import Path

def get_title(file_path):
    tree = html.parse(file_path)
    title_path = '/html/body/div[2]/main/div/div[3]/section/div/div[1]/div/div[2]/hgroup/h1'
    title = tree.xpath(title_path)[0].text
    return title

def save_to_csv(data, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data])

def main():
    file_path = 'downloaded_pages/imdb.html'
    title = get_title(file_path)
    save_to_csv(title, 'scraped_data.csv')

if __name__ == "__main__":
    main()