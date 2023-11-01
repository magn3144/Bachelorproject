import csv
from lxml import html

def scrape_myspace():
    page_path = 'downloaded_pages/myspace.html'
    xpath = '/html/body/div[1]/div[2]/div[1]/section[1]/div[2]/article[1]/div/div[2]/form/header/h3'
    
    with open(page_path, 'r') as f:
        page_content = f.read()

    tree = html.fromstring(page_content)
    elements = tree.xpath(xpath)
    
    names = []
    for element in elements:
        names.append(element.text)

    with open('scraped_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name'])
        for name in names:
            writer.writerow([name])

scrape_myspace()