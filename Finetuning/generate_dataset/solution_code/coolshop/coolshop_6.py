import csv
from lxml import html


def scrape_brands():
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Brand', 'Link'])
        
        with open('downloaded_pages/coolshop.html', 'r') as file:
            page_content = file.read()
            tree = html.fromstring(page_content)
            
            brand_elements = tree.xpath('//ul[contains(@class, "product-brands")]//li/a')
            
            for element in brand_elements:
                brand = element.text.strip() if element.text else ''
                link = element.get('href', '')
                
                writer.writerow([brand, link])


scrape_brands()