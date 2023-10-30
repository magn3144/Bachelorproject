import csv
from lxml import etree

def scrape_labels(html_file_path):
    tree = etree.parse(html_file_path)
    root = tree.getroot()

    labels = root.xpath("//label")
    rows = [("Label",)]
    for label in labels:
        text = label.text.strip() if label.text else ""
        rows.append((text,))

    with open("scraped_data.csv", "w", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

scrape_labels("downloaded_pages/woman.html")