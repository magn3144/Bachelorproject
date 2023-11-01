import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/artstation.html', 'r') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all form labels with class "form-label bs-control-label"
labels = tree.xpath('//label[contains(@class, "form-label bs-control-label")]')

# Extract the text from each label
label_text = [label.text for label in labels]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Labels'])
    writer.writerows([[label] for label in label_text])