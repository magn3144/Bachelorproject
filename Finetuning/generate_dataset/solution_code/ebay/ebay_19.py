import csv
from lxml import etree

def scrape_subtitle(html_path):
    tree = etree.parse(html_path)
    subtitle_xpath = '/html/body/div[4]/div[2]/section/div[1]/div[2]/h2'
    subtitle_element = tree.xpath(subtitle_xpath)[0]
    subtitle = subtitle_element.text.strip()
    return subtitle

def save_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Subtitle'])
        writer.writerow([data])

html_path = 'downloaded_pages/ebay.html'
subtitle = scrape_subtitle(html_path)
save_csv(subtitle, 'scraped_data.csv')