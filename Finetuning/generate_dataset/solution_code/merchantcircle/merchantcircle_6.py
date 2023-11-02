import csv
from lxml import html

# Open the HTML file and parse it
with open('downloaded_pages/merchantcircle.html', 'r') as file:
    content = file.read()
tree = html.fromstring(content)

# Find all the category names using XPath
category_elements = tree.xpath('//h2//a/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category'])
    for category in category_elements:
        writer.writerow([category])