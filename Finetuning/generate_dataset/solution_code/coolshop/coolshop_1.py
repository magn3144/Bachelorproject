import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/coolshop.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Extract the titles of the latest visited products
latest_products = tree.xpath('//div[@class="product-carousel-title"]/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Latest Visited Products'])
    writer.writerows(zip(latest_products))