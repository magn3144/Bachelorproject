import csv
from lxml import etree

# Helper function to extract text content from an element, given its XPath
def extract_text(element, xpath):
    el = element.xpath(xpath)
    if el:
        return el[0].text.strip()
    return ''

# Helper function to extract attributes from an element, given its XPath and attribute name
def extract_attribute(element, xpath, attribute):
    el = element.xpath(xpath)
    if el:
        return el[0].get(attribute, '').strip()
    return ''

# Read the HTML file
with open('downloaded_pages/cnn.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all the article elements
articles = tree.xpath('//div[contains(@class, "cd__content")]')

# Create a list to store the extracted data
data = []

# Extract the image credits for each article
for article in articles:
    image_credit = extract_text(article, './/figcaption[@class="image__credit"]')
    data.append({'Image Credit': image_credit})

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Image Credit'])
    writer.writeheader()
    writer.writerows(data)