import csv
from lxml import etree

def save_data_to_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def get_heading_content(html_path):
    tree = etree.parse(html_path)
    root = tree.getroot()

    faq_headings = root.xpath('//h3[contains(@class, "faq__list__item__question")]')
    faq_content = root.xpath('//div[contains(@class, "faq__list__item__answer__text")]')

    data = [['Heading', 'Content']]
    for heading, content in zip(faq_headings, faq_content):
        data.append([heading.text.strip(), content.text.strip()])

    return data

data = get_heading_content('downloaded_pages/ældresagen.html')
save_data_to_csv(data)