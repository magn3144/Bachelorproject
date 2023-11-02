import csv
from lxml import etree

# Define the XPath for the website name
website_name_xpath = '/html/body/div/header[2]/div/a/h1'

# Read the HTML file
with open('downloaded_pages/stackexchange-hot-questions.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find the website name using XPath
website_name = tree.xpath(website_name_xpath)[0].text.strip()

# Save the website name as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Website Name'])
    writer.writerow([website_name])