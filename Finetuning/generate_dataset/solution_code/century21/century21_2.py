import csv
from pathlib import Path
from lxml import html

# Set the local path to the HTML file
html_file_path = 'downloaded_pages/century21.html'

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the element with text "My C21 Account"
element = tree.xpath("//h3[contains(text(), 'My C21 Account')]")[0]

# Get the text
text = element.text_content().strip()

# Save the scraped data as CSV
data = [['My C21 Account', text]]
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)