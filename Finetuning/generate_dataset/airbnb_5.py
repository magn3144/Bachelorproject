import csv
import lxml.html as lh

with open('downloaded_pages/airbnb.html', 'r') as file:
    page_content = file.read()

tree = lh.fromstring(page_content)

locations = tree.xpath('//div[contains(@class, "t1jojoys dir dir-ltr")]/text()')
links = tree.xpath('//a[contains(@class, "l1ovpqvx c1kblhex dir dir-ltr")]/@href')

data = zip(locations, links)

with open('scraped_data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(data)