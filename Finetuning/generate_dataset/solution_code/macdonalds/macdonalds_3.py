import csv
from lxml import etree

# Define the XPath expressions for the section titles
xpaths = [
    '/html/body/div[1]/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/nav/ul[2]/li/a/span',
    '/html/body/div[1]/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/section/div[2]/div/h1',
    '/html/body/div[1]/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/section/div[3]/ul/li[2]/a/div/div/div[2]',
    '/html/body/div[1]/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/section/div[3]/ul/li[5]/a/div/div/div[1]',
    '/html/body/div[1]/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/section/div[3]/ul/li[6]/a/div/div/div[1]'
]

# Open the HTML file and create an XML parser
with open('downloaded_pages/macdonalds.html', 'r') as file:
    html = file.read()
parser = etree.HTMLParser()
tree = etree.HTML(html, parser)

# Scrape the section titles using the XPath expressions
titles = [tree.xpath(xpath)[0].text.strip() for xpath in xpaths]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Section Title'])
    writer.writerows([[title] for title in titles])