import csv
from lxml import etree

def extract_text_from_html():
    page_path = 'downloaded_pages/ebay.html'
    
    with open(page_path, 'r') as file:
        content = file.read()

    html_tree = etree.HTML(content)
    results_pagination = html_tree.xpath('/html/body/div[4]/div[4]/div[3]/section/div[2]/nav/span/h2/text()')[0]

    data = [['Results Pagination']]
    data.append([results_pagination])

    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == "__main__":
    extract_text_from_html()