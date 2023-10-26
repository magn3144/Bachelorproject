import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/accuweather.html', 'r') as file:
    content = file.read()

# Parse the HTML
tree = html.fromstring(content)

# Find all footer category section links
footer_links = tree.xpath('//a[@class="footer-category-section-link"]/text()')

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Footer Category Section Links'])
    for link in footer_links:
        writer.writerow([link])