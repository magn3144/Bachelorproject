import csv
from lxml import etree

def extract_text_from_element(element):
    return ''.join(element.xpath('.//text()')).strip()

html_file = 'downloaded_pages/globestudios.html'
xpath = '/html/body/div/div[4]/footer/div[1]/div[3]/div/div[2]/form/fieldset/div/label'

# Open HTML file
with open(html_file, 'r', encoding='utf-8') as file:
    html = file.read()

# Parse HTML
tree = etree.HTML(html)

# Extract text from element using xpath
element = tree.xpath(xpath)[0]
text = extract_text_from_element(element)

# Write scraped data to CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([text])