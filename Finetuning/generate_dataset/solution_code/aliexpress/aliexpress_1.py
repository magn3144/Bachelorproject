import csv
from lxml import etree

# Define the target HTML file path
html_file = 'downloaded_pages/aliexpress.html'

# Define the list of HTML elements and their corresponding XPaths
elements = [
    {
        'element': 'a',
        'xpath': '/html/body/div[6]/div[1]/div/div[2]/div/div[2]/div[3]/a[34]/div[2]/span/a'
    },
    {
        'element': 'a',
        'xpath': '/html/body/div[6]/div[1]/div/div[2]/div/div[2]/div[3]/a[5]/div[2]/span/a'
    }
]

# Function to extract text based on XPath
def extract_text(element, xpath):
    elements = root.xpath(xpath)
    if elements:
        return elements[0].text.strip()
    return None

# Open the HTML file and create an ElementTree
with open(html_file, 'r') as file:
    html = file.read()
    parser = etree.HTMLParser()
    tree = etree.parse(html, parser)
    root = tree.getroot()

# Extract data for each element
data = []
for element in elements:
    text = extract_text(element['element'], element['xpath'])
    data.append(text)

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Store Name'])
    for d in data:
        writer.writerow([d])