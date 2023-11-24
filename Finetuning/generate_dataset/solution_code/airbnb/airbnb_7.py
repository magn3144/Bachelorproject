import csv
from lxml import html

file_path = 'downloaded_pages/airbnb.html'

with open(file_path, 'r') as file:
    page_content = file.read()

tree = html.fromstring(page_content)

# Get the parent element of the header menu items
parent_element = tree.xpath('//*[@id="categoryScroller"]/div/div/div/div[3]/div/div/div/div/..')[0]

# Get the header menu items
header_menu_items1 = parent_element.xpath('//label[@class="c1rmt9x7 dir dir-ltr"]')
header_menu_items2 = parent_element.xpath('//label[@class="c1rmt9x7 c3nt6z6 dir dir-ltr"]')

# Get the text of the header menu items with child elements
header_menu_items_text1 = [item.text_content() for item in header_menu_items1 if item.xpath('.//text()')]
header_menu_items_text2 = [item.text_content() for item in header_menu_items2 if item.xpath('.//text()')]
header_menu_items_text = header_menu_items_text1 + header_menu_items_text2

# Save the data to a CSV file in one column
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Cabins"])
    for item in header_menu_items_text:
        writer.writerow([item])