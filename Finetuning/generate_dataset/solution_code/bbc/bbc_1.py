import csv
from lxml import html

def scrape_headlines():
    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Headline"])

        with open("downloaded_pages/bbc.html", "r", encoding="utf-8") as file:
            html_doc = file.read()

        tree = html.fromstring(html_doc)

        headlines = tree.xpath(
            '//span[contains(@class, "gs-c-promo-heading__title")]/text()')
        for headline in headlines:
            writer.writerow([headline])

scrape_headlines()