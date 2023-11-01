import csv
from pathlib import Path
from lxml import etree


def get_page_text(html_file, xpath):
    with open(html_file, 'r') as f:
        content = f.read()
    parser = etree.HTMLParser()
    tree = etree.fromstring(content, parser)
    elements = tree.xpath(xpath)
    return [element.text for element in elements]


def save_to_csv(data):
    headers = ['Text']
    rows = [[text] for text in data]
    with open('scraped_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


if __name__ == "__main__":
    html_file = Path("downloaded_pages/top.html")
    p_xpath = "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div/div[2]/div/article[3]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[3]/a[2]/span/span/div/div/p"
    data = get_page_text(html_file, p_xpath)
    save_to_csv(data)