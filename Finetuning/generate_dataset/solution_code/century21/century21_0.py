import csv
from lxml import etree

def parse_listing_price(html_file):
    tree = etree.parse(html_file)
    listing_prices = tree.xpath('//a[@class="listing-price"]/text()')
    details = tree.xpath('//div[@class="pdp-listing-type sale"]/text()')
    return list(zip(listing_prices, details))

def save_data_as_csv(data):
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Listing Price', 'Details'])
        writer.writerows(data)

html_file = 'downloaded_pages/century21.html'
scraped_data = parse_listing_price(html_file)
save_data_as_csv(scraped_data)