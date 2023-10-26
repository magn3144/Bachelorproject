import csv
from lxml import etree


def extract_text(html_element):
    return html_element.text.strip() if html_element is not None else ''


def get_page_data():
    with open('downloaded_pages/bloomberg.html', 'rb') as file:
        html = file.read()
    return etree.HTML(html)


def get_company_names(page_data):
    company_name_elements = page_data.xpath('//a[contains(@class, "bb-that-category__link")]')
    company_names = [extract_text(element) for element in company_name_elements]
    return company_names


def get_product_names(page_data):
    product_name_elements = page_data.xpath('//span[contains(text(), "Bloomberg the Company")]')
    product_names = [extract_text(element) for element in product_name_elements]
    return product_names


def save_data_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Company Name', 'Product Name'])
        writer.writerows(data)


def main():
    page_data = get_page_data()
    company_names = get_company_names(page_data)
    product_names = get_product_names(page_data)
    data = list(zip(company_names, product_names))
    save_data_to_csv(data)


if __name__ == '__main__':
    main()