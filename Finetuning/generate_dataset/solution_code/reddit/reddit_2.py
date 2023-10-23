import csv
from datetime import datetime
from lxml import etree

html_file = 'downloaded_pages/reddit.html'
xpath = '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[138]/div/div/div/div[2]/div[2]/div[1]/span/a'

tree = etree.parse(html_file)
root = tree.getroot()

data = []

elements = root.xpath(xpath)
for element in elements:
    date_string = element.text
    date = datetime.strptime(date_string, '%Y-%m-%d').date()
    data.append(date)

with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for date in data:
        writer.writerow([date])