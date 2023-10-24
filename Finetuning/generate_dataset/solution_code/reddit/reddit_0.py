import csv
from lxml import etree

def extract_titles(html_file):
    tree = etree.parse(html_file)
    titles = tree.xpath("//h3[@class='title']/a/text()")
    return titles

def save_to_csv(data, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title'])
        writer.writerows(data)

html_file = 'downloaded_pages/reddit.html'
csv_file = 'scraped_data.csv'

titles = extract_titles(html_file)
save_to_csv(titles, csv_file)