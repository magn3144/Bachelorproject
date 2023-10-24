import csv
from lxml import etree

def scrape_stock_names(html_file_path):
    tree = etree.parse(html_file_path)
    root = tree.getroot()

    stock_names = set()

    for xpath in [
        "/html/body//span",
        "/html/body//a",
        "/html/body//h1",
        "/html/body//h2",
        "/html/body//h3",
        "/html/body//h4",
        "/html/body//h5",
        "/html/body//h6",
        "/html/body//p",
        "/html/body//li",
        "/html/body//td",
        "/html/body//th",
        "/html/body//div",
    ]:
        elements = root.xpath(xpath)
        for element in elements:
            if element.text and len(element.text.strip()) > 0:
                stock_names.add(element.text.strip())

    with open("scraped_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Stock Names"])
        writer.writerows([[stock_name] for stock_name in stock_names])

scrape_stock_names("downloaded_pages/reddit.html")