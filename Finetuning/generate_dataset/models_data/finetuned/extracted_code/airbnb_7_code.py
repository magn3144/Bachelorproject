
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find all the header menu items
header_items = tree.xpath('//*[@id="header-menu"]/div/div/div/div/ul/li/a/span/text()')

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Category'])
    writer.writerows([[item]] for item in header_items)
