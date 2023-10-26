import csv
from lxml import etree

def scrape_data():
    html_file = "downloaded_pages/dk.indeed.html"
    category = "Jobs"
    xpath_list = [
        ("/html/head/title", "title"),
        ("/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div[2]/div/div/ul/li/span/a", "link"),
    ]

    tree = etree.parse(html_file, etree.HTMLParser())
    data = []

    for xpath, column_name in xpath_list:
        elements = tree.xpath(xpath)
        for element in elements:
            data.append({column_name: element.text})

    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

scrape_data()