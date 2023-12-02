import csv
from lxml import html

with open('downloaded_pages/airbnb.html', 'r') as f:
    page = f.read()

tree = html.fromstring(page)

support_xpaths = [
    '/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[1]/ul/li/a'
]

hosting_xpaths = [
    '/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[2]/ul/li/a'
]

airbnb_xpaths = [
    '/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/ul/li/a'
]

links = []

for xpath in support_xpaths:
    links.append(tree.xpath(xpath + '/@href'))

for xpath in hosting_xpaths:
    links.append(tree.xpath(xpath + '/@href'))

for xpath in airbnb_xpaths:
    links.append(tree.xpath(xpath + '/@href'))

with open('scraped_data.csv', 'w') as f:
    writer = csv.writer(f)
    for link in links:
        writer.writerow(link)