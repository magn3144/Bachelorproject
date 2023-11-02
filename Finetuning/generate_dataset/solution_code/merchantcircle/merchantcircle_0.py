import csv
from lxml import etree

def extract_data(html_file, elements):
    tree = etree.parse(html_file)
    data = []
    
    for element, xpath in elements.items():
        result = tree.xpath(xpath)
        if result:
            data.append((element, result[0].text))
            
    return data

html_file = 'downloaded_pages/merchantcircle.html'

elements = {
    'business_name': '/html/body/div[1]/div[4]/section/div/div/h2/a',
    'phone_number': '/html/body/div[1]/div[4]/section/div/div/div[1]/div[2]/span'
}

data = extract_data(html_file, elements)

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Business Name', 'Phone Number'])
    writer.writerows(data)