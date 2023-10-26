import csv
from lxml import etree

# Define the XPaths of the elements we want to scrape
title_xpath = "/html/head/title"
order_xpath = "//h3[contains(text(),'Order & Purchases')]/following-sibling::ul[1]/li/a/text()"
purchase_xpath = "//h3[contains(text(),'Order & Purchases')]/following-sibling::ul[2]/li/a/text()"

# Load the HTML file
html_file = "downloaded_pages/bestbuy.html"
tree = etree.parse(html_file)

# Scrape the data
title_element = tree.xpath(title_xpath)[0]
order_elements = tree.xpath(order_xpath)
purchase_elements = tree.xpath(purchase_xpath)

# Prepare the data to write in CSV format
data = [
    ['Page Title', 'Order', 'Purchase'],
    [title_element.text, ', '.join(order_elements), ', '.join(purchase_elements)]
]

# Write the data to CSV file
with open('scraped_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)