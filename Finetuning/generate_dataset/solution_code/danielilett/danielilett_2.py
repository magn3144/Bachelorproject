import csv
from lxml import html

# Define the target HTML file path
html_path = 'downloaded_pages/danielilett.html'

# Define the target elements and their XPaths
elements = [
    {'element': 'p', 'xpath': '/html/body/div[3]/div/div/article/p[387]'},
    {'element': 'p', 'xpath': '/html/body/div[3]/div/div/article/p[97]'},
    {'element': 'p', 'xpath': '/html/body/div[3]/div/div/article/p[387]'},
    {'element': 'p', 'xpath': '/html/body/div[3]/div/div/article/p[3]'},
    {'element': 'p', 'xpath': '/html/body/div[3]/div/div/article/p[344]'},
    {'element': 'p', 'xpath': '/html/body/div[3]/div/div/article/p[8]'},
    {'element': 'p', 'xpath': '/html/body/div[3]/div/div/article/p[223]'},
    {'element': 'p', 'xpath': '/html/body/div[3]/div/div/article/p[200]'},
    {'element': 'p', 'xpath': '/html/body/div[3]/div/div/article/p[372]'},
    {'element': 'p', 'xpath': '/html/body/div[3]/div/div/article/p[130]'}
]

# Scrape the data
data = []
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()
    tree = html.fromstring(content)
    for element in elements:
        paragraph = tree.xpath(element['xpath'])
        if paragraph:
            data.append([element['element'], element['xpath'], paragraph[0].text_content()])

# Save the data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Element', 'XPath', 'Content'])
    writer.writerows(data)