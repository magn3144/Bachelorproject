import csv
from lxml import etree

def scrape_text_from_h1(local_path):
    tree = etree.parse(local_path)
    element = tree.xpath("/html/body/div/div/div/div[1]/div[1]/div[2]/h1")[0]
    scraped_text = element.text

    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Website', 'Category', 'Scraped Text'])
        writer.writerow(['top', 'Digital Websites', scraped_text])

scrape_text_from_h1('downloaded_pages/top.html')