import csv
from lxml import etree

# Define the XPath expressions for the span tags
xpaths = [
    "/html//span",
    "//span",
    "//span[@class='my-class']"
]

# Load the HTML file
html_file = 'downloaded_pages/flyingtiger.html'
with open(html_file, 'r') as f:
    html = f.read()

# Parse the HTML
root = etree.HTML(html)

# Scrape the text inside the span tags
scraped_data = []
for xpath in xpaths:
    span_elements = root.xpath(xpath)
    for element in span_elements:
        text = element.text.strip() if element.text else ''
        scraped_data.append(text)

# Save the scraped data as a CSV file
csv_file = 'scraped_data.csv'
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Scraped Data'])
    writer.writerows([[data] for data in scraped_data])