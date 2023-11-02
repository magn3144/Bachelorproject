import csv

from lxml import etree


def scrape_listing_details(html, xpath):
    tree = etree.parse(html)
    elements = tree.xpath(xpath)
    listing_details = [element.text.strip() for element in elements]
    return listing_details


def save_data_as_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


if __name__ == '__main__':
    html = "downloaded_pages/homefinder.html"
    xpath = "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[6]/a/div[1]/div[2]/div[1]"
    scraped_data = scrape_listing_details(html, xpath)
    save_data_as_csv(scraped_data, "scraped_data.csv")