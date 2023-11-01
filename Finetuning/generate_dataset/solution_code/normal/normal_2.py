import csv
import requests
from lxml import etree

def extract_data():
    # Load the HTML file
    with open('downloaded_pages/normal.html', 'r', encoding='utf-8') as file:
        html_data = file.read()
    
    # Parse the HTML
    parser = etree.HTMLParser()
    tree = etree.fromstring(html_data, parser)
    
    # Extract product images and descriptions
    product_images = tree.xpath('//img[@class="product-image"]/@src')
    product_descriptions = tree.xpath('//div[@class="product-description"]/text()')
    
    # Prepare the data as a list of tuples
    scraped_data = list(zip(product_images, product_descriptions))
    
    # Save the data as a CSV file
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Image', 'Description'])
        writer.writerows(scraped_data)

if __name__ == "__main__":
    extract_data()