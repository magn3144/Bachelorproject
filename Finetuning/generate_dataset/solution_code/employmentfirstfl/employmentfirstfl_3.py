import csv
from lxml import etree

tree = etree.parse('downloaded_pages/employmentfirstfl.html')
root = tree.getroot()

h2_elements = root.xpath('/html/body/div/div/div/main/article/div/h2')
h2_texts = [element.text for element in h2_elements]

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['h2_text'])
    writer.writerows(zip(h2_texts))