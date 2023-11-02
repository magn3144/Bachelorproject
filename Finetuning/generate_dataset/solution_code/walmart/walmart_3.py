import csv
import requests
from lxml import html

# Load the HTML file
html_path = "downloaded_pages/walmart.html"
with open(html_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find all fresh produce items
produce_items = tree.xpath("//h3[contains(., 'Fresh')]")

# Extract the prices of fresh produce items
produce_prices = []
for item in produce_items:
    price_element = item.xpath("./following-sibling::div[contains(@class, 'mr1') or contains(@class, 'f7') or contains(@class, 'f6')]")
    if price_element:
        price = price_element[0].text_content().strip()
        produce_prices.append(price)

# Save the scraped data as a CSV file
csv_path = "scraped_data.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Item", "Price"])  # Write header
    for i in range(len(produce_items)):
        writer.writerow([produce_items[i].text_content().strip(), produce_prices[i]])  # Write each item and its price