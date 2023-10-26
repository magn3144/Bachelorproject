import csv

from lxml import html


def scrape_webpage(elements):
    with open('downloaded_pages/ziprecruiter.html') as file:
        page = file.read()
    
    tree = html.fromstring(page)
    
    data = {}
    
    for element in elements:
        text = tree.xpath(element['xpath'] + '/text()')[0]
        data[element['name']] = text
    
    return data


def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Global Terms of Use Agreement', data['Global Terms of Use Agreement']])
    

elements = [
    {'name': 'Global Terms of Use Agreement', 'xpath': '/html/body/footer/div/div[2]/ul/li[4]/a'}
]

scraped_data = scrape_webpage(elements)
save_to_csv(scraped_data)