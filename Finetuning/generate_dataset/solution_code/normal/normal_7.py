import csv
from lxml import etree

def scrape_web_page():
    # Load the HTML file
    html_file = 'downloaded_pages/normal.html'
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Parse the HTML using lxml
    parser = etree.HTMLParser()
    tree = etree.parse(html_file, parser)
    
    # Retrieve all product discounts, sales prices, and expiration dates
    discounts_xpath = '//*[@class="discount"]'
    sales_prices_xpath = '//*[@class="sales-price"]'
    expiration_dates_xpath = '//*[@class="expiration-date"]'
    
    discounts = tree.xpath(discounts_xpath)
    sales_prices = tree.xpath(sales_prices_xpath)
    expiration_dates = tree.xpath(expiration_dates_xpath)
    
    # Save scraped data as CSV file
    csv_file = 'scraped_data.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Discount', 'Sales Price', 'Expiration Date'])
        
        for discount, sales_price, expiration_date in zip(discounts, sales_prices, expiration_dates):
            writer.writerow([discount.text, sales_price.text, expiration_date.text])

# Run the web scraping function
scrape_web_page()