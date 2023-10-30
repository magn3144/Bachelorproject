import csv
from lxml import etree

def extract_text_from_html(path, xpath):
    with open(path, 'rb') as file:
        tree = etree.parse(file)
    element = tree.xpath(xpath)
    text = element[0].text.strip()
    return text

html_path = 'downloaded_pages/globestudios.html'
xpath = '/html/body/div/div[3]/div[6]/div/div/div[1]/div/div/p'
text = extract_text_from_html(html_path, xpath)

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])
    writer.writerow([text])