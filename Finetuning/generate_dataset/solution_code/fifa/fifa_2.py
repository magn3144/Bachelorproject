import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/fifa.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = etree.HTML(html_content)

# Find all tournament names
tournament_elements = tree.xpath('//h2[contains(@class, "ff-text-custom")]/text()')
tournament_names = [element.strip() for element in tournament_elements]

# Save the tournament names in a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tournament Name'])
    writer.writerows(zip(tournament_names))