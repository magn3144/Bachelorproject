import csv
from lxml import etree

def get_element_text(tree, xpath):
    elements = tree.xpath(xpath)
    if elements:
        return elements[0].text.strip()
    else:
        return ""

def scrape_page(html_file):
    with open(html_file, 'r') as file:
        html = file.read()
    
    tree = etree.HTML(html)
    scraped_data = get_element_text(tree, '/html/body/div[3]/div/div/div[8]/div/div/div/div[1]/div[2]/a[5]/div/div[1]')
    
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([scraped_data])

scrape_page('downloaded_pages/census.html')