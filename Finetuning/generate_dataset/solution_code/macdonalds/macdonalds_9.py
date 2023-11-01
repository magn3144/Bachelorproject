```python
import csv
from lxml import html

# Path to the downloaded HTML file
html_path = "downloaded_pages/macdonalds.html"

# XPaths for the category and product elements
category_xpath = "//span[@class='category-title' and text()='Kolde Drikke']"
product_xpath = "//div[contains(@class, 'cmp-category__item-name')]"

# Parse the HTML file
with open(html_path, 'r') as file:
    html_content = file.read()
tree = html.fromstring(html_content)

# Find the category
category_element = tree.xpath(category_xpath)
if not category_element:
    raise ValueError("Category not found")
category_name = category_element[0].text.strip()

# Find the products
product_elements = tree.xpath(product_xpath)
products = [(element.text.strip(), tree.getpath(element)) for element in product_elements]

# Save the scraped data as a CSV file
csv_path = "scraped_data.csv"
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Product Name", "XPath"])
    writer.writerow([category_name, "", ""])  # Space for category name in the CSV
    for product in products:
        writer.writerow([category_name] + list(product))
        
print("Scraping completed successfully")