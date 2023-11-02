import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/investing.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find all stock names using XPath
stock_names = tree.xpath('//div[@class="crypto-coins-table_cellNameText__aaXmK"]/text()')

# Save the stock names as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Stock Name'])
    writer.writerows([[stock_name] for stock_name in stock_names])