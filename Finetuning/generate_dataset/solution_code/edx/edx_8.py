import csv
from lxml import etree

html_file = 'downloaded_pages/edx.html'
output_file = 'scraped_data.csv'
xpaths = {
    'education_level': '/html/body/div[1]/div[1]/div/main/div/div[8]/div[3]/div/div/div/div/div[5]/div[2]/p'
}

with open(html_file, 'r') as file:
    html = file.read()

tree = etree.HTML(html)
education_level = tree.xpath(xpaths['education_level'])[0].text.strip()

data = [{'Education Level': education_level}]

with open(output_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Education Level'])
    writer.writeheader()
    writer.writerows(data)