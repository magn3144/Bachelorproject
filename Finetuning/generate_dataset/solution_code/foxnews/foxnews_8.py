import csv
from lxml import etree

def write_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def scrape_html(source_path, xpath):
    with open(source_path, 'r') as file:
        html = file.read()
    tree = etree.HTML(html)
    elements = tree.xpath(xpath)
    return [element.text for element in elements]

def main():
    source_path = 'downloaded_pages/foxnews.html'
    xpaths = [
        '/html/body/div/div[2]/main[2]/section/div/article/a/div/span',
        '/html/body/div/div[2]/main[2]/section/div/article/span[@class="kicker-text"]',
        '/html/body/div/div[2]/main[2]/section/div/article/span[@class="time"]'
    ]
    data = []
    
    for xpath in xpaths:
        scraped_data = scrape_html(source_path, xpath)
        data.append(scraped_data)
    
    write_to_csv(data)

if __name__ == '__main__':
    main()