import csv
from scrapy import Selector

def scrape_page(html_file_path, elements):
    with open(html_file_path, 'r') as file:
        html_content = file.read()
    selector = Selector(text=html_content)
    
    scraped_data = []
    for element, xpath in elements.items():
        selected_elements = selector.xpath(xpath)
        for selected_element in selected_elements:
            text = selected_element.xpath('.//text()').get(default='')
            scraped_data.append((text, xpath))
    
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Text', 'XPath'])
        writer.writerows(scraped_data)

elements = {
    'p1': '/html/body/c-wiz/div/div[2]/main/div[2]/c-wiz/section/div[1]/div[2]/p[1]',
    'p2': '/html/body/c-wiz/div/div[2]/main/div[2]/c-wiz/section/div[1]/div[2]/p[2]',
    'p3': '/html/body/c-wiz/div/div[2]/main/div[2]/c-wiz/section/div[1]/div[2]/p[3]',
    # Add more 'p' elements and their corresponding xpaths if needed
}

scrape_page('downloaded_pages/google news.html', elements)