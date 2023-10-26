import csv
from lxml import etree

def extract_text(html_path, xpath):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = etree.parse(f)
        element = html.xpath(xpath)
        if element:
            return element[0].text
        else:
            return ""

def main():
    html_path = "downloaded_pages/ebay.html"
    xpath = "/html/body/div[4]/div[2]/nav/ol/li[2]/span"
    scraped_data = extract_text(html_path, xpath)
    
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Breadcrumb Trail'])
        writer.writerow([scraped_data])

if __name__ == "__main__":
    main()