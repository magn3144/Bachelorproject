import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/aboutus.html', 'r') as file:
    html_string = file.read()

# Parse the HTML string
tree = html.fromstring(html_string)

# Find all labels on the page
labels = tree.xpath("//label/text()")

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Label"])
    writer.writerows([[label] for label in labels])