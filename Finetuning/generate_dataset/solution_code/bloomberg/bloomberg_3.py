import csv
from lxml import etree

# Define the XPaths for the live now story descriptions
xpaths = [
    "/html/body/div[1]/div[2]/div[2]/div[2]/nav/div[2]/ul/li[1]/div/section[2]/article/div[2]/a[1]/p",
    "/html/body/div[1]/div[2]/div[2]/div[2]/nav/div[2]/ul/li[1]/div/section[2]/article/div[2]/a[2]/p",
    "/html/body/div[1]/div[2]/div[2]/div[2]/nav/div[2]/ul/li[1]/div/section[2]/article/div[2]/a[3]/p",
    "/html/body/div[1]/div[2]/div[2]/div[2]/div[5]/div[3]/div/section/section/section[2]/article[1]/div/div[2]/p",
    "/html/body/div[1]/div[2]/div[2]/div[2]/div[5]/div[3]/div/section/section/section[2]/article[2]/div/div[2]/p"
]

# Load the HTML file
with open('downloaded_pages/bloomberg.html', 'rb') as f:
    html = f.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.HTML(html, parser)

# Find the live now story descriptions using the XPaths
descriptions = []
for xpath in xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        descriptions.append(element.text)

# Save the descriptions as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Description'])
    writer.writerows([[description] for description in descriptions])