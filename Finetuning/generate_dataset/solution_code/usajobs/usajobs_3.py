import csv
import requests
from lxml import etree

# Load the HTML file
with open('downloaded_pages/usajobs.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = etree.HTML(html_content)

# Find all agency names using XPath
agency_elements = tree.xpath("//h4[@class='usajobs-search-result--core__agency']")
agency_names = [element.text.strip() for element in agency_elements]

# Save the agency names as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Agency Name'])
    for name in agency_names:
        writer.writerow([name])