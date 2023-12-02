import csv
from lxml import html

with open("downloaded_pages/DTU_entrepreneurship.html", "r") as file:
    page_content = file.read()

tree = html.fromstring(page_content)

headings = tree.xpath('//h2[contains(@class,"a-heading-h1 o-hero__title")]/text()')

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for heading in headings:
        writer.writerow([heading])