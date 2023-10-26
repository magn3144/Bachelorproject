import csv
from lxml import etree

def extract_category():
    file_path = "downloaded_pages/avsforum.html"
    target_category_xpath = "/html/body/div[1]/header/div/div/div[2]/a/h1"
    
    with open(file_path, "r") as f:
        html_content = f.read()
    
    parser = etree.HTMLParser()
    tree = etree.fromstring(html_content, parser)
    
    category_element = tree.xpath(target_category_xpath)[0]
    category_name = category_element.text.strip()
    
    with open("scraped_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Category Name"])
        writer.writerow([category_name])