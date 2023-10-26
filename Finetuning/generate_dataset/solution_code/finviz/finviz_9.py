import csv
from lxml import etree

# Load the HTML file
html_path = 'downloaded_pages/finviz.html'
with open(html_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# XPaths of the links
link_xpaths = [
    '/html/body/div[1]/form/button/div/a',
    '/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody//a',
    '/html/body/div[6]/div/div/a'
]

# Extract the links
links = []
for xpath in link_xpaths:
    link_elements = tree.xpath(xpath)
    for element in link_elements:
        links.append(element.text)

# Save the links as CSV
csv_path = 'scraped_data.csv'
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Links'])
    writer.writerows([[link] for link in links])