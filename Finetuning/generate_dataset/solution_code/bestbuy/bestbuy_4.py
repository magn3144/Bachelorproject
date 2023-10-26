import csv
from lxml import etree

def scrape_page(html_path):
    tree = etree.parse(html_path)
    root = tree.getroot()

    offerings = []

    # Find all offerings of Playstation 4 and Playstation 5
    xpath_ps4 = "//span[contains(text(), 'PlayStation 4') or contains(text(), 'PlayStation 5')]/ancestor::li"
    ps4_elements = root.xpath(xpath_ps4)

    for element in ps4_elements:
        offering = {}

        # Get the product title
        xpath_title = ".//a[contains(@class, 'product-title')]"
        title_element = element.xpath(xpath_title)[0]
        offering['title'] = title_element.text.strip() if title_element.text else ""

        # Get the product price
        xpath_price = ".//div[contains(@class, 'priceView-hero-price')]"
        price_element = element.xpath(xpath_price)[0]
        offering['price'] = price_element.text.strip() if price_element.text else ""

        # Add the offering to the list
        offerings.append(offering)

    # Save the scraped data as CSV
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'price'])
        writer.writeheader()
        writer.writerows(offerings)

# Run the script
scrape_page('downloaded_pages/bestbuy.html')