import csv
from lxml import html

file_path = 'downloaded_pages/airbnb.html'

with open(file_path, 'r') as file:
    page_content = file.read()

tree = html.fromstring(page_content)
header_menu_items = tree.xpath('//div[@class="header-browse-menu"]/ul/li/a/text()')

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Types"])
    for element in header_menu_items:
        writer.writerow([element])