import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/aliexpress.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the pagination element using XPath
pagination_element = tree.xpath('/html/body/div[6]/div[1]/div/div[2]/div/div[2]/div[4]/div[1]/ul/li[contains(@class, "pagination--isActive")]/text()')

# Save scraped pagination number as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category', 'Pagination Number'])
    writer.writerow(['E-commerce', pagination_element[0] if pagination_element else 'N/A'])