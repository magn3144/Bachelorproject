import csv
from lxml import etree

def parse_html_file(file_path):
    with open(file_path, 'r') as file:
        return etree.HTML(file.parse(file))

def extract_dates(html_tree):
    date_elements = html_tree.xpath("//*[contains(text(), '–')]")
    dates = [el.text for el in date_elements if el.text.count('–') == 1]
    return dates

def save_to_csv(data, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

html_tree = parse_html_file('downloaded_pages/airbnb.html')
dates = extract_dates(html_tree)
save_to_csv(dates, 'scraped_data.csv')