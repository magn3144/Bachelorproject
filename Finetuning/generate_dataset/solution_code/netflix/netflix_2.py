import csv
from lxml import etree

def get_text_of_category(html_path, category_xpath):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    tree = etree.HTML(html)
    category_element = tree.xpath(category_xpath)
    if category_element:
        category_text = category_element[0].text.strip()
    else:
        category_text = ""
    return category_text

html_path = "downloaded_pages/netflix.html"
category_xpath = "/html/body/div[1]/div/div[2]/main/section[5]/h2"
category_text = get_text_of_category(html_path, category_xpath)

with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Text'])
    writer.writerow(['New Releases', category_text])