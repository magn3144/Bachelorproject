import csv
import lxml.html

def extract_data(html_path):
    with open(html_path, 'r') as f:
        html = f.read()

    tree = lxml.html.fromstring(html)

    headlines = tree.xpath('//span[@class="container__headline-text"]/text()')
    urls = tree.xpath('//span[@class="container__headline-text"]/ancestor::a/@href')

    data = zip(headlines, urls)

    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Headline', 'URL'])
        writer.writerows(data)

extract_data('downloaded_pages/cnn.html')