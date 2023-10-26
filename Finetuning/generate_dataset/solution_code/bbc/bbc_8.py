import csv
from lxml import etree

def extract_titles(html_path, category):
    tree = etree.parse(html_path)
    root = tree.getroot()
    
    if category == 'News':
        article_titles = root.xpath("//h3[contains(@class, 'gs-c-promo-heading__title') and contains(@class, 'nw-o-link-split__text') and contains(text(), 'Belgians race boats made of giant pumpkins')]/text()")
    else:
        article_titles = []
    
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title'])
        for title in article_titles:
            writer.writerow([title])

html_path = 'downloaded_pages/bbc.html'
category = 'News'
extract_titles(html_path, category)