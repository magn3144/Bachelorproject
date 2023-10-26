import csv
from lxml import html

def scrape_breadcrumb():
    file_path = 'downloaded_pages/ebay.html'
    with open(file_path, 'r') as file:
        content = file.read()
    tree = html.fromstring(content)
    breadcrumb = tree.xpath('/html/body/div[4]/div[2]/nav/ol/li/span/text()')
    
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Breadcrumb"])
        for item in breadcrumb:
            writer.writerow([item])

scrape_breadcrumb()