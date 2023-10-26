import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/dice.html', 'r') as f:
    html_data = f.read()

# Parse the HTML data
root = etree.HTML(html_data)

# Find all the company addresses
company_addresses = root.xpath('//span[@class="search-result-location"]/text()')

# Write the scraped data to CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Company Address'])  # Write header
    for address in company_addresses:
        writer.writerow([address])  # Write data row