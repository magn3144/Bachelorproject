import csv
from lxml import etree

def get_privacy_links(html_file):
    with open(html_file, 'r', encoding="utf-8") as file:
        tree = etree.parse(file)
    
    privacy_links = tree.xpath('//a[text()="Privacy"]/@href')
    
    return privacy_links

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Privacy Policy Links'])
        writer.writerows([[link] for link in data])

if __name__ == '__main__':
    html_file = 'downloaded_pages/tumblr.html'
    privacy_links = get_privacy_links(html_file)
    save_to_csv(privacy_links, 'scraped_data.csv')