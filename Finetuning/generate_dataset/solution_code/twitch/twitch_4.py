```
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/twitch.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Define the XPath for product names
product_name_xpath = '//*[@class="product-name"]//text()'

# Define the XPath for prices
price_xpath = '//*[@class="price"]//text()'

# Get the product names and prices
product_names = tree.xpath(product_name_xpath)
prices = tree.xpath(price_xpath)

# Ensure the number of product names and prices are the same
if len(product_names) == len(prices):
    # Prepare data for writing to CSV file
    data = list(zip(product_names, prices))

    # Write data to CSV file
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Product Name', 'Price'])
        writer.writerows(data)
else:
    print("Error: Number of product names and prices do not match.")
```