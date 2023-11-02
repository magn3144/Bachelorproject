import csv
from lxml import etree

def extract_neighborhoods(html_path):
    tree = etree.parse(html_path)
    neighborhoods = tree.xpath(
        '//label[contains(text(), "Neighborhoods")]/following-sibling::ul/li/a/text()')
    
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Neighborhood'])
        writer.writerows([[neighborhood] for neighborhood in neighborhoods])

html_path = 'downloaded_pages/homefinder.html'
extract_neighborhoods(html_path)