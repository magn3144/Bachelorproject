import csv
from urllib.parse import urljoin
from lxml import etree

def scrape_menu_links(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    tree = etree.HTML(html)

    links = tree.xpath("//header//a[@class='h-mobile-header__burger-menu-list-link']")
    data = []
    for link in links:
        text = link.text.strip()
        xpath = tree.getpath(link)
        category = tree.xpath(xpath + "/text()")[0].strip()

        data.append([text, category])

    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Link', 'Category'])
        writer.writerows(data)

html_path = 'downloaded_pages/ældresagen.html'
scrape_menu_links(html_path)