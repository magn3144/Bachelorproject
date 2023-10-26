import csv
from lxml import etree


def scrape_authors(html_file_path):
    tree = etree.parse(html_file_path)
    xpath = "/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[3]/div/article/a/h3"
    element = tree.xpath(xpath)[0]
    authors = element.text.split(", ")
    
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Author'])
        for author in authors:
            writer.writerow([author])


scrape_authors('downloaded_pages/nytimes.html')