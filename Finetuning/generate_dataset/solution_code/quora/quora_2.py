import csv
from lxml import etree

def extract_data(html_file, xpaths):
    data = []
    parser = etree.HTMLParser()
    tree = etree.parse(html_file, parser)

    for xpath in xpaths:
        elements = tree.xpath(xpath)
        for element in elements:
            title = element.text.strip()
            answer = element.getnext().text.strip()
            data.append([title, answer])

    return data

def save_data(data):    
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Answer'])
        writer.writerows(data)

html_file = 'downloaded_pages/quora.html'
xpaths = [
    '/html/body/div[1]/div/p',
    # Add more xpaths here for other elements if needed
]

scraped_data = extract_data(html_file, xpaths)
save_data(scraped_data)