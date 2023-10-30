import csv
from lxml import html

def extract_author_names():
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Author']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        tree = html.parse('downloaded_pages/bog & ide.html')

        authors = tree.xpath('//span[@class="eieez5y3 css-jr2gsl-StyledText-Author e1w70fa50"]/text()')

        for author in authors:
            writer.writerow({'Author': author})