import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/merchantcircle.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the labels from the search form
labels = tree.xpath("//form//label/text()")

# Write the labels to the CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Labels'])
    writer.writerows([[label] for label in labels])