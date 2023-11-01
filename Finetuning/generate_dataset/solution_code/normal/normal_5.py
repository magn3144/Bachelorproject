import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/normal.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Extract the product information
product_elements = tree.xpath('//div[@class="product"]')

# Create the CSV file and write the header
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product Name', 'Availability', 'Quantity'])

    # Write each product's information to the CSV file
    for product_element in product_elements:
        product_name = product_element.xpath('.//h3/text()')[0]
        availability = product_element.xpath('.//span[@class="availability"]/text()')[0]
        quantity = product_element.xpath('.//span[@class="quantity"]/text()')[0]
        writer.writerow([product_name, availability, quantity])