import csv
import requests
from lxml import html

# Define the target HTML file path
html_file_path = "downloaded_pages/normal.html"

# Load the HTML file
with open(html_file_path, "r") as file:
    content = file.read()

# Parse the HTML content
tree = html.fromstring(content)

# Extract the shop website's shipping information
shipping_info = tree.xpath("//h2[contains(text(), 'Shipping')]//following-sibling::p//text()")

# Prepare the data for CSV
data = [["Shipping Information"]]
data.extend([[info.strip()] for info in shipping_info])

# Save the scraped data as CSV
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)