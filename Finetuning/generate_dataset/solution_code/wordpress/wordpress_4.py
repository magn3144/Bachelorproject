import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/wordpress.html', 'r') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Define the XPaths
xpath = '/html/body/div/footer/nav/ul[3]/li[2]/a'

# Find the target element
element = tree.xpath(xpath)[0]

# Extract the text
text = element.text

# Save the text as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([text])