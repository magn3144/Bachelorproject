import csv
from lxml import etree

def scrape_webpage(html_path, xpath):
    with open(html_path, 'r') as file:
        html_content = file.read()
        
    tree = etree.HTML(html_content)
    elements = tree.xpath(xpath)
    
    return [element.text for element in elements]

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Melons'])
        for element in data:
            writer.writerow([element])

html_path = 'downloaded_pages/walmart.html'
xpaths = [
    '/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[3]/div/div/div/section/div/div/h2[2]',
    '/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[3]/div/div/div/section/div/div/p[6]'
]

scraped_data = []
for xpath in xpaths:
    scraped_data += scrape_webpage(html_path, xpath)

save_to_csv(scraped_data)