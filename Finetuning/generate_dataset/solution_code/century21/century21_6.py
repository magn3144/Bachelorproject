import csv
from lxml import etree

def scrape_location(path):
    tree = etree.parse(path)
    location_element = tree.xpath('/html/body/div[1]/header/div/nav/div[1]/div/ul/li[1]/div/ul/li[3]/a/span')[0]
    location = location_element.text.strip()
    
    with open('scraped_data.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Location'])
        writer.writerow([location])

scrape_location('downloaded_pages/century21.html')