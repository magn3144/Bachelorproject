import csv
from lxml import etree

# Define the XPaths for the elements on the target page
xpaths = {
    'label': '/html/body/div[3]/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div[1]/div/label'
}

# Define the local path to the HTML file
html_file_path = 'downloaded_pages/ebay.html'

# Load the HTML file
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Create the parser and parse the HTML content
parser = etree.HTMLParser()
tree = etree.parse(html_file_path, parser)

# Scrape the data using the XPaths
scraped_data = {}
for key, xpath in xpaths.items():
    elements = tree.xpath(xpath)
    
    if elements:
        scraped_data[key] = elements[0].text.strip()
    else:
        scraped_data[key] = ""

# Write the scraped data to a CSV file
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=list(scraped_data.keys()))
    writer.writeheader()
    writer.writerow(scraped_data)