import csv
from lxml import etree

# Function to extract text from HTML element based on XPath
def extract_text(element, xpath):
    if element is not None:
        node = element.xpath(xpath)
        if len(node) > 0:
            return node[0].text.strip() if node[0].text else ""
    return ""

# Function to save scraped data into a CSV file
def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Link Text'])
        for row in data:
            writer.writerow(row)

# Read the local HTML file
with open('downloaded_pages/bestbuy.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find all link texts related to gaming products
links = tree.xpath("//a[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'gaming')]")

# Extract the link texts
scraped_data = [[link.text] for link in links]

# Save the scraped data into a CSV file
save_to_csv(scraped_data)