import csv
from lxml import etree

html_file = 'downloaded_pages/globestudios.html'
output_file = 'scraped_data.csv'

def extract_text_from_element(element):
    return element.text.strip()

def save_data_to_csv(data):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Text'])
        for item in data:
            writer.writerow([item])

tree = etree.parse(html_file)
root = tree.getroot()

# XPath for the element containing the desired text
xpath = "/html/body/div/div[4]/footer/div[1]/div[3]/div/div[1]"
element = root.xpath(xpath)[0]

# Extract and save the text
text = extract_text_from_element(element)
save_data_to_csv([text])