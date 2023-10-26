import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/etsy.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Scrape product names
product_names = tree.xpath('//div[contains(@class, "wt-pl-xs-10") or contains(@class, "truncate_after_two_lines")]/text()')

# Scrape prices
prices = tree.xpath('//span[contains(@class, "currency-value")]/text()')

# Combine product names and prices
data = zip(product_names, prices)

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Price'])
    writer.writerows(data)