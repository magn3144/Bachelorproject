import csv
from lxml import etree


def scrape_page(category, elements, file_path):
    tree = etree.parse(file_path)
    tags = []

    for element, xpath in elements.items():
        elements_found = tree.xpath(xpath)
        for el in elements_found:
            tags.append(el.text)

    with open('scraped_data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Category', 'Tag'])
        for tag in tags:
            writer.writerow([category, tag])


category = "Video game Websites"

elements = {
    "Football": "/html/body/div[1]/div[1]/div/div[2]/div/div/ul/li[4]/a/div",
}

file_path = "downloaded_pages/y8.html"

scrape_page(category, elements, file_path)