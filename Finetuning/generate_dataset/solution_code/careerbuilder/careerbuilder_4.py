import csv
from lxml import etree

def get_footer_info(tree):
    footer_elements = tree.xpath('/html/body/div[1]/div/div[2]/footer/div[2]/div')
    footer_data = []
    
    for element in footer_elements:
        footer_data.append(element.text.strip())
    
    return footer_data

file_path = 'downloaded_pages/careerbuilder.html'
category = 'Jobs'

with open(file_path, 'r') as file:
    html = file.read()

tree = etree.HTML(html)
footer_info = get_footer_info(tree)

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Footer Information'])
    writer.writerow([category, '\n'.join(footer_info)])