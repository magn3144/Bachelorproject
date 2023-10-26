import csv
import os.path
from lxml import etree

def find_elements(tree, xpath):
    elements = tree.xpath(xpath)
    return [element.text.strip() if element is not None and element.text is not None else '' for element in elements]

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Title'])
        writer.writerows(data)

# Define the xpaths for the sections 'Happening Today' and 'Opinion'
happening_today_xpath = '/html/body/div/div[2]/div[2]/main/div[2]/article[5]/div[1]/span'
opinion_xpath = '/html/body/div/div[2]/div[3]/main/div[1]/div/article[6]/div[1]/span'

# Load the HTML file
html_path = 'downloaded_pages/foxnews.html'
if os.path.isfile(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        html = file.read()

    # Parse the HTML
    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)

    # Scrape the data
    happening_today = find_elements(tree, happening_today_xpath)
    opinion = find_elements(tree, opinion_xpath)

    # Save the scraped data to CSV
    data = [('Happening Today', item) for item in happening_today] + [('Opinion', item) for item in opinion]
    save_to_csv(data)