import csv
from lxml import html

def scrape_data():
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name'])

        tree = html.parse('downloaded_pages/coursera.html')

        elements = [
            ('class', 'cds-119'),
            ('class', 'cds-121')
        ]

        for element in elements:
            elements_with_text = tree.xpath(f"//*[contains({element[0]}, '{element[1]}')]/text()")
            for text in elements_with_text:
                writer.writerow([text])
    
scrape_data()