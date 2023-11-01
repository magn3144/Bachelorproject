import csv
from lxml import etree

# Function to extract data from HTML
def extract_data():
    # Load HTML file
    with open('downloaded_pages/flyingtiger.html', 'r') as file:
        html = file.read()

    # Create an XML tree from the HTML
    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)

    # Find all product names and prices
    product_names = tree.xpath('//h2[@class="image-with-text__heading"]/text()')
    product_prices = tree.xpath('//span[@class="subtitle--s price-item price-item--regular"]/text()')

    # Create a list of scraped data
    scraped_data = list(zip(product_names, product_prices))

    # Return the scraped data
    return scraped_data

# Function to save data as CSV
def save_as_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name', 'Price'])
        writer.writerows(data)

# Main function
def main():
    # Extract data from HTML
    scraped_data = extract_data()

    # Save data as CSV
    save_as_csv(scraped_data)

# Run the main function
if __name__ == "__main__":
    main()