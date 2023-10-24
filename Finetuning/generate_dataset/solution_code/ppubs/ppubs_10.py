import csv
from lxml import html

# Define the list of HTML elements and their corresponding XPaths
elements = [
    {'element': 'p', 'xpath': '/html/body/div[3]/div/div/div[2]/p[2]'},
    {'element': 'h4', 'xpath': '/html/body/div[2]/div/div/div/div[2]/h4'},
    {'element': 'h1', 'xpath': '/html/body/div[2]/div/section[1]/div/div[1]/div/div[1]/div/div/h1'},
    {'element': 'h1', 'xpath': '/html/body/div[3]/div/div/div[1]/h1'},
    {'element': 'h2', 'xpath': '/html/body/div[2]/div/section[1]/div/div[1]/div/div[4]/div/div/form/h2'},
    {'element': 'h2', 'xpath': '/html/body/div[2]/div/section[1]/div/div[1]/div/div[3]/div/div/h2'},
    {'element': 'label', 'xpath': '/html/body/div[2]/div/section[1]/div/div[1]/div/div[2]/div/div/form/div/label'},
    {'element': 'label', 'xpath': '/html/body/div[2]/div/section[1]/div/div[1]/div/div[4]/div/div/form/div[2]/div/div/label'},
    {'element': 'h5', 'xpath': '/html/body/div[2]/div/section[1]/div/div[2]/div/div/div[2]/h5'},
    {'element': 'li', 'xpath': '/html/body/div[3]/div/div/div[2]/ol/li[3]'},
    {'element': 'li', 'xpath': '/html/body/div[2]/div/section[1]/div/div[2]/div/div/div[2]/ol/li[1]'},
    {'element': 'th', 'xpath': '/html/body/div[2]/div/section[2]/div/div/div/div/div[2]/div/table/thead/tr/th[5]'},
    {'element': 'td', 'xpath': '/html/body/div[2]/div/section[2]/div/div/div/div/div[2]/div/table/tbody/tr[5]/td[4]'},
    {'element': 'td', 'xpath': '/html/body/div[2]/div/section[2]/div/div/div/div/div[2]/div/table/tbody/tr[38]/td[1]'},
    {'element': 'p', 'xpath': '/html/body/div[2]/div/section[1]/div/div[2]/div/div/div[2]/p[1]'},
    {'element': 'span', 'xpath': '/html/body/header/div[1]/nav/a/span'}
]

# Parse the HTML file
with open('downloaded_pages/ppubs.html', 'r') as file:
    content = file.read()
tree = html.fromstring(content)

# Scrape the error messages or hints and store them in a list
scraped_data = []
for element in elements:
    text_list = tree.xpath(element['xpath'] + '/text()')
    text = ' '.join(text_list).strip()
    scraped_data.append({'element': element['element'], 'text': text})

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['element', 'text'])
    writer.writeheader()
    writer.writerows(scraped_data)