import csv
from lxml import etree

def extract_text(element):
    if element.text:
        return element.text.strip()
    else:
        return ""

def scrape_html(local_path):
    with open(local_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    parser = etree.HTMLParser()
    tree = etree.fromstring(html_content, parser)

    paragraphs = tree.xpath("//p")
    divs = tree.xpath("//div")

    data = []
    for element in paragraphs + divs:
        text = extract_text(element)
        if text:
            data.append({"text": text})

    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["text"]
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        writer.writerows(data)

scrape_html("downloaded_pages/jysk.html")