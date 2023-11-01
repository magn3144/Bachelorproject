from bs4 import BeautifulSoup
import csv

html_file_path = 'downloaded_pages/google news.html'

with open(html_file_path, 'r') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

span_elements = soup.find_all('span', class_='VfPpkd-StrnGf-rymPhb-b9t22c')

scraped_data = []
for span in span_elements:
    text = span.text.strip()
    xpath = soup.find(text=text).parent.xpath
    scraped_data.append((text, xpath))

csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Text', 'XPath'])
    writer.writerows(scraped_data)