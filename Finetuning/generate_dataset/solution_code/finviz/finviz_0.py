import csv
from lxml import html

# Load the HTML file
file_path = 'downloaded_pages/finviz.html'
with open(file_path, 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Extract stock names
stock_names = tree.xpath('//a[@class="tab-link"]/text()')

# Write the stock names to a CSV file
csv_path = 'scraped_data.csv'
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Stock Name'])
    for name in stock_names:
        writer.writerow([name])