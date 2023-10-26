import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/finviz.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find all instances of text within span tags
span_elements = tree.xpath('//span/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])
    writer.writerows([[text] for text in span_elements])