import csv
from lxml import html

def extract_logo_information():
    with open('downloaded_pages/DTU-entrepreneurship.html', 'r') as file:
        content = file.read()
    tree = html.fromstring(content)
    logos = tree.xpath('//span[@class="sitetextlogo"]/text()')
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Logo'])
        for logo in logos:
            writer.writerow([logo])

extract_logo_information()