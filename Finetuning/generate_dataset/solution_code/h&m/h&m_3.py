import csv
from lxml import etree

# Read the HTML file
with open("downloaded_pages/h&m.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Create an XML tree from the HTML content
parser = etree.HTMLParser()
tree = etree.fromstring(html_content, parser)

# Find all product names using XPath
product_names = tree.xpath("//h2[@class='d1cd7b a09145 e07e0d a04ae4']/text()")

# Save the product names as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name'])
    writer.writerows(zip(product_names))