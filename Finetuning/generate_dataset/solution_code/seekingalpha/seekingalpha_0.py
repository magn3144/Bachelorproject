import csv
from lxml import etree

# Define the HTML elements and their corresponding XPaths
elements = [
    {
        'element': 'title',
        'xpath': '/html/head/title',
    },
    {
        'element': 'news_headline',
        'xpath': '/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[1]/div/div[2]/section/div/div[1]/div/div/h1',
    },
    {
        'element': 'news_headline',
        'xpath': '/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[*]/div/div/h3/a',
    }
]

# Load the HTML file
with open('downloaded_pages/seekingalpha.html', 'r') as file:
    html_string = file.read()

# Parse the HTML
html = etree.HTML(html_string)

# Scrape the data
data = []
for element in elements:
    element_data = {
        'element': element['element'],
        'content': html.xpath(element['xpath'])[0].text.strip(),
    }
    data.append(element_data)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['element', 'content'])
    writer.writeheader()
    writer.writerows(data)