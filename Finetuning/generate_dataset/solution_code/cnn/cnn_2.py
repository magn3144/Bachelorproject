import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/cnn.html', 'r') as file:
    page_content = file.read()

# Parse the HTML content
tree = html.fromstring(page_content)

# Retrieve the category title in the header section
category_title = tree.xpath('/html/body/header/div/div[1]/h1/text()')[0]

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category Title'])
    writer.writerow([category_title])