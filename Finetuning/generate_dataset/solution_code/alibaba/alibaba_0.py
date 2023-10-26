import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/alibaba.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Extract product names, prices, and sell points
product_names = tree.xpath('//span[contains(@class, "search-card-e-sell-point")]/text()')
prices = tree.xpath('//div[contains(@class, "search-card-e-price-main")]/text()')
sell_points = tree.xpath('//span[contains(@class, "search-card-m-sale-features__item")]/text()')

# Zip the scraped data together
scraped_data = zip(product_names, prices, sell_points)

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Price', 'Sell Point'])
    writer.writerows(scraped_data)