import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/danielilett.html'
category = 'Forums and Review Sites'

meta_data = []

with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    post_meta_elements = soup.find_all(class_='post-meta')
    for element in post_meta_elements:
        meta_data.append({
            'Content': element.text.strip(),
            'XPath': element.parent.name,
        })

with open('scraped_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Content', 'XPath', 'Category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in meta_data:
        data['Category'] = category
        writer.writerow(data)