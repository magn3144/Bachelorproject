import csv
from lxml import etree

# Define the local path to the HTML file
html_path = 'downloaded_pages/normal.html'

# Define the XPaths for the product variations
xpaths = [
    "//div[contains(@class, 'product')]/h2",
    "//div[contains(@class, 'product')]/div[contains(@class, 'sizes')]/span",
    "//div[contains(@class, 'product')]/div[contains(@class, 'flavors')]/span"
]

# Function to scrape the webpage and extract product variations
def scrape_webpage(html_path, xpaths):
    # Load the HTML file
    with open(html_path, 'r') as file:
        html_content = file.read()

    # Parse the HTML content
    root = etree.HTML(html_content)

    # Extract product variations using XPaths
    product_variations = []
    for xpath in xpaths:
        elements = root.xpath(xpath)
        variations = [element.text.strip() for element in elements if element.text is not None]
        product_variations.append(variations)

    return product_variations

# Scrape the webpage
product_variations = scrape_webpage(html_path, xpaths)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for variations in product_variations:
        writer.writerow(variations)