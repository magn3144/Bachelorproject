import csv
from lxml import html

def scrape_product_data():
    # Load the HTML file
    with open('downloaded_pages/h&m.html', 'r') as file:
        html_content = file.read()

    # Parse the HTML content
    tree = html.fromstring(html_content)

    # Scrape product names and prices
    product_names = tree.xpath('//h2[@class="d1cd7b a09145 e07e0d a04ae4"]/text()')
    product_prices = tree.xpath('//span[@class="aeecde ac3d9e b19650"]/text()')

    # Save data to a CSV file
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name', 'Price'])

        for name, price in zip(product_names, product_prices):
            writer.writerow([name.strip(), price.strip()])

if __name__ == "__main__":
    scrape_product_data()