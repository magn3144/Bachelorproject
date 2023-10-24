import csv
from lxml import etree

def get_total_results(tree):
    results = tree.xpath('//span[@id="pageInfo"]/text()')
    if results:
        total_results = results[0].split()[-1]
        return total_results
    else:
        return ''

def get_element_path(element):
    return etree.ElementTree(element).getpath(element)

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Page", "XPath", "Total Results"])
        writer.writerows(data)

def scrape_page(html_file):
    tree = etree.parse(html_file)
    data = []
    
    for element in tree.iter():
        if element.text and element.text.strip() in ['Page', 'Total Results']:
            page = element.text.strip()
            xpath = get_element_path(element)
            total_results = get_total_results(tree)
            data.append([page, xpath, total_results])
    
    save_to_csv(data)

scrape_page('downloaded_pages/ppubs.html')