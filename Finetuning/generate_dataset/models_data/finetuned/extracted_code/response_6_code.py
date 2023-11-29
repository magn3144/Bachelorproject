import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find the elements with the label "Persons"
persons_elements = tree.xpath('//label[text()="Persons"]')

# Extract the text from the elements
persons = [e.text for e in persons_elements]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(persons)
