import csv
from lxml import etree

# Load the HTML file
html_file = 'downloaded_pages/redfin.html'
with open(html_file, 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# Extract property addresses
addresses = tree.xpath('//span[contains(@class, "collapsedAddress")]/text()')

# Save the scraped data as a CSV file
csv_file = 'scraped_data.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Address'])

    for address in addresses:
        writer.writerow([address])