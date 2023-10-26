import csv
from lxml import etree

# Define the XPath expressions for design-related items
design_xpath = "//a[contains(., 'Design') or contains(., 'design')]/text()"

# Parse the HTML file
html = etree.parse('downloaded_pages/coursera.html', etree.HTMLParser())

# Extract the names of design-related items
design_items = html.xpath(design_xpath)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Design Items'])
    writer.writerows([[item] for item in design_items])