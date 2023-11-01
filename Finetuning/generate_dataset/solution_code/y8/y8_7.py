from lxml import html
import csv

# Read the HTML file
with open('downloaded_pages/y8.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find the technology type "HTML5"
elements = tree.xpath('//p[@class="html5"]/text()')

# Save the scraped data as CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Technology Type'])
    for element in elements:
        writer.writerow([element.strip()])