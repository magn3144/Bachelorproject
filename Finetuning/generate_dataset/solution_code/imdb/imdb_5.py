import csv
import lxml.html as lh
import os

path = "downloaded_pages/imdb.html"
doc = lh.fromstring(open(path).read())

nav_elements = doc.xpath('//*[@id="navMenu1"]/div[2]/ul/li')
nav_dict = {'Site Options': [], 'Links': []}

for element in nav_elements:
    nav_text = element.xpath('.//a/text()')
    link = element.xpath('.//a/@href')

    if nav_text and link: 
        nav_dict['Site Options'].append(nav_text[0])
        nav_dict['Links'].append(link[0])

with open('scraped_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Site Options', 'Links']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows([{'Site Options': n, 'Links': l} for n, l in zip(nav_dict['Site Options'], nav_dict['Links'])])