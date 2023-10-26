import csv
from lxml import etree

def get_element_value(html, xpath):
    element = html.xpath(xpath)
    if element:
        return element[0].text.strip() if element[0].text else ''
    return ''

def main():
    # Read the HTML file
    with open('downloaded_pages/aliexpress.html', 'r', encoding='utf-8') as f:
        contents = f.read()

    # Parse the HTML
    html = etree.HTML(contents)

    # Scrape the product title
    product_title = get_element_value(html, '/html/body/div[6]/div[1]/div/div[2]/div/div[2]/div[3]/a[18]/div[2]/div[3]/h1')

    # Save scraped data as a CSV file
    with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Product Title'])
        writer.writerow([product_title])

if __name__ == '__main__':
    main()