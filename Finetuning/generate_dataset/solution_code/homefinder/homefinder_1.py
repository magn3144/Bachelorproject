import csv
from lxml import etree

def extract_address(html_file):
    tree = etree.parse(html_file)
    address_element = tree.xpath('/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[30]/a/div[1]/div[2]/div[1]')[0]
    address = address_element.text.strip()
    
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Address'])
        writer.writerow([address])

html_file = 'downloaded_pages/homefinder.html'
extract_address(html_file)