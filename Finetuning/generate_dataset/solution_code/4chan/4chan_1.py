import csv
from lxml import etree


def get_categories_xpaths(file_path):
    with open(file_path, "r") as f:
        html_content = f.read()

    root = etree.HTML(html_content)
    elements = root.xpath("//*")
    categories_xpaths = []

    for element in elements:
        if element.text:
            category = element.text.strip()
            xpath = root.getpath(element)
            categories_xpaths.append((category, xpath))

    with open("scraped_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Category", "XPath"])
        writer.writerows(categories_xpaths)


get_categories_xpaths("downloaded_pages/4chan.html")