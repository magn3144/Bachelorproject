import csv
from lxml import html

# Define the local path to the HTML file
html_file = 'downloaded_pages/aboutus.html'

# Define the XPaths for the list items
list_items_xpath = "//li"

# Parse the HTML file
with open(html_file, 'r') as f:
    content = f.read()
tree = html.fromstring(content)

# Find all list items
list_items = tree.xpath(list_items_xpath)

# Prepare the data to be saved in CSV file
data = []
for li in list_items:
    data.append(li.text_content())

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['List Items'])
    for item in data:
        writer.writerow([item])