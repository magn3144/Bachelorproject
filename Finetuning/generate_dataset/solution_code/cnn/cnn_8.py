import csv
from lxml import etree

# Define the target HTML file path
html_file_path = 'downloaded_pages/cnn.html'

# Define the XPaths for the subnav section links in the footer
xpaths = [
    '/html/body/div[1]/div[5]/div/div/footer/div/div[3]/nav/ul/li[1]/a',
    '/html/body/div[1]/div[5]/div/div/footer/div/div[3]/nav/ul/li[2]/a',
    '/html/body/div[1]/div[5]/div/div/footer/div/div[3]/nav/ul/li[3]/a',
    '/html/body/div[1]/div[5]/div/div/footer/div/div[3]/nav/ul/li[4]/a',
    '/html/body/div[1]/div[5]/div/div/footer/div/div[3]/nav/ul/li[5]/a'
]

# Create an empty list to store the scraped data
scraped_data = []

# Parse the HTML file
tree = etree.parse(html_file_path)

# Iterate over the XPaths and extract the text content of each element
for xpath in xpaths:
    elements = tree.xpath(xpath)
    if elements:
        text = elements[0].text.strip()
        scraped_data.append(text)
    else:
        scraped_data.append('')

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Subnav Section Links'])
    writer.writerows(zip(scraped_data))