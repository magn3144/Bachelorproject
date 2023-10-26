import csv
from lxml import etree

def scrape_footer(html_file, xpath):
    with open(html_file, "r") as file:
        html = file.read()
    
    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)
    
    footer_elements = tree.xpath(xpath)
    footer_text = [elem.text.strip() for elem in footer_elements]
    
    with open("scraped_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Copyright"])
        writer.writerows([[text] for text in footer_text])

scrape_footer("downloaded_pages/fifa.html", "/html/body/div/div/div[2]/footer/div/section[3]/div/div[2]")