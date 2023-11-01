import csv
from lxml import etree

def scrape_page(html_path, xpath):
    with open(html_path, "r") as f:
        html = f.read()

    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)

    elements = tree.xpath(xpath)

    return [element.text.strip() for element in elements]

if __name__ == '__main__':
    html_path = "downloaded_pages/twitter.html"
    xpath = "/html/body/div/div/div/div[2]/form/div/div/span"

    data = scrape_page(html_path, xpath)

    with open('scraped_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Scraped Data"])
        writer.writerow(data)