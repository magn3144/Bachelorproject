import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/usajobs.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# Find the sorting options
sorting_options = tree.xpath('//label[@class="usajobs-search-controls__sort-label"]/text()')

# Write the sorting options to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Sorting Options'])
    for option in sorting_options:
        writer.writerow([option])