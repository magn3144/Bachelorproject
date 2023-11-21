import csv
import os
from lxml import html, etree

class XpathScraper:

    def __init__(self, html_file_path):
        self.html_file_path = html_file_path
        self.tree = self._load_html()
        
    def _load_html(self):
        with open(self.html_file_path, 'r') as file:
            src = file.read()
        return html.fromstring(src)

    def get_links_from_section(self, section):
        xpath = f'//h3[text()="{section}"]/following-sibling::ul[1]/li/a/@href'
        return self.tree.xpath(xpath)


scraper = XpathScraper('downloaded_pages/airbnb.html')
sections = ['Support', 'Hosting', 'Airbnb']

data = {}
for section in sections:
    data[section] = scraper.get_links_from_section(section)

longest_list_len = max(len(data[section]) for section in sections)

# Normalize list lengths
for section in sections:
    data[section].extend([''] * (longest_list_len - len(data[section])))

with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(sections)
    writer.writerows(zip(*data.values()))
