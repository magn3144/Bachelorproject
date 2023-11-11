import csv
from lxml import etree

def scrape_sitemap(html_file):
    tree = etree.parse(html_file)
    namespaces = {'html': 'http://www.w3.org/1999/xhtml'}
    sitemap_elements = tree.xpath('//html:a[@class="_r243u8q l1ovpqvx dir dir-ltr"]', namespaces=namespaces)
    
    sitemap_data = []
    for element in sitemap_elements:
        data = element.text
        sitemap_data.append(data)

    with open('scraped_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Sitemap Data"])
        writer.writerows([[data] for data in sitemap_data])

scrape_sitemap('downloaded_pages/airbnb.html')