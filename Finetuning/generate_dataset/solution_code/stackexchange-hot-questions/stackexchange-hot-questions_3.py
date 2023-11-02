import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/stackexchange-hot-questions.html', 'r') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find the "Loading..." element using XPath
loading_element = tree.xpath('/html/body/div/header[1]/div/form/div/div/div[2]/div/div')[0]

# Extract the text content of the "Loading..." element
loading_text = loading_element.text.strip()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([loading_text])