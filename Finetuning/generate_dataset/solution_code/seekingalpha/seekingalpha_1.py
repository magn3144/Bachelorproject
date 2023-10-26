import csv
import os
from pathlib import Path
from lxml import etree


def get_timestamps(html_path):
    with open(html_path, "r") as file:
        html_data = file.read()

    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html_data), parser)
    root = tree.getroot()

    timestamps = []
    elements = root.xpath("//span[@class='kD_Bq kD_is']")
    for element in elements:
        timestamps.append(element.text.strip())

    return timestamps


html_file_path = os.path.join("downloaded_pages", "seekingalpha.html")
timestamps = get_timestamps(html_file_path)

csv_file_path = "scraped_data.csv"
with open(csv_file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp"])
    writer.writerows([[timestamp] for timestamp in timestamps])