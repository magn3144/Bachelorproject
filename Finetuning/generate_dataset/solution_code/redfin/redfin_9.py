import csv
from lxml import etree

# Define the target HTML file path
file_path = 'downloaded_pages/redfin.html'

# Define the XPaths for the desired elements
xpaths = [
    '/html/body//p',
]

# Function to extract text using XPath
def extract_text(element, xpath):
    if xpath.startswith('//'):
        return element.xpath(xpath)
    else:
        return element.xpath(xpath)[0].text

# Parse the HTML file
tree = etree.parse(file_path)
root = tree.getroot()

# Extract text from the HTML elements using XPaths
data = []
for xpath in xpaths:
    elements = extract_text(root, xpath)
    data.extend(elements)

# Save the extracted data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])
    writer.writerows([[text] for text in data])