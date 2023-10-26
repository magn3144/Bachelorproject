import csv
from lxml import etree

html_file = "downloaded_pages/dice.html"

def scrape_posted_dates():
    tree = etree.parse(html_file)

    posted_dates = tree.xpath("//span[contains(@class, 'posted-date')]/text()")

    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Posted Date'])
        for date in posted_dates:
            writer.writerow([date])

scrape_posted_dates()