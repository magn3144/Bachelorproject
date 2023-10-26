import csv
from lxml import etree

# Load HTML file
with open("downloaded_pages/etsy.html", "r") as f:
    html_text = f.read()

# Create HTML tree
tree = etree.HTML(html_text)

# Retrieve text content of men's hoodies title
title_element = tree.xpath('/html/body/main/div/div[1]/div/div[2]/div[1]/div[2]/div/div/h1')[0]
hoodies_title = title_element.text.strip()

# Save scraped data as CSV
data = [['Category', 'Task', 'Text Content'],
        ['E-commerce', "Retrieve men's hoodies title", hoodies_title]]

with open('scraped_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)