import csv
from lxml import etree

def get_text_from_element(element):
    if element is not None:
        return element.text
    else:
        return ""

def scrape_webpage(html_file):
    with open(html_file, 'r') as file:
        html_data = file.read()
    
    parser = etree.HTMLParser()
    tree = etree.fromstring(html_data, parser)
    
    comments = tree.xpath("//p[contains(@class, '_1qeIAgB0cPwnLhDF9XSiJM')]")
    
    data = []
    for comment in comments:
        text = get_text_from_element(comment)
        data.append([text])
    
    return data

def save_data_as_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Comment'])
        writer.writerows(data)

html_file = 'downloaded_pages/reddit.html'
scraped_data = scrape_webpage(html_file)
save_data_as_csv(scraped_data)