import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/y8.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# Define the XPaths
xpaths = [
    '/html/body/div[4]/div/div/div[2]/p[2]/a[3]',
    '/html/body/div[1]/div[5]/div[2]/ul/li[11]/a/div[2]/div[3]',
    '/html/body/div[1]/div[5]/div[2]/ul/li[8]/a/div[2]/div[2]/span',
    '/html/body/div[4]/div/div/div[3]/p[2]/a[2]',
    '/html/body/div[1]/div[2]/div/div/div/div[2]/ul/li[15]/a',
]

# Extract the text using XPaths
data = []
for xpath in xpaths:
    elements = tree.xpath(xpath)
    if elements:
        text = elements[0].text.strip()
        data.append(text)

# Save the extracted data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Multiplayer Games"])
    for item in data:
        writer.writerow([item])