import csv
import re
from lxml import etree

def extract_featured_articles(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    tree = etree.HTML(html)

    featured_articles_xpath = "//span[contains(@id, 'From_today')]/text()"
    featured_articles = tree.xpath(featured_articles_xpath)

    clean_articles = [re.sub(r'\[.*\]', '', article).strip() for article in featured_articles]

    return clean_articles

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Featured Articles'])
        for article in data:
            writer.writerow([article])

if __name__ == '__main__':
    html_file = 'downloaded_pages/wikipedia.html'
    featured_articles = extract_featured_articles(html_file)
    save_to_csv(featured_articles)