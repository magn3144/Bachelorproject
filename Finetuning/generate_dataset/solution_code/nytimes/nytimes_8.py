import csv
from lxml import etree

def get_text(node):
    return ''.join(node.xpath('.//text()')).strip()

def save_as_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Advertisement Text'])
        writer.writerows(data)

def scrape_advertisement_text(html_path):
    tree = etree.parse(html_path)
    root = tree.getroot()
    
    advertisements = root.xpath("//p[contains(., 'Advertisement') or contains(., 'Sponsored Content')]")
    advertisement_text = [get_text(ad) for ad in advertisements]
    
    save_as_csv(advertisement_text)

scrape_advertisement_text("downloaded_pages/nytimes.html")