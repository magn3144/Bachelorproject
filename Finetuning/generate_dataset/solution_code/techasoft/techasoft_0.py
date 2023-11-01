import csv
from lxml import etree

# Load the HTML file
with open('downloaded_pages/techasoft.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create a list to store the extracted data
scraped_data = []

# Parse the HTML content
tree = etree.HTML(html_content)

# Find all the article submission sites
submission_sites = tree.xpath('//div[@class="col-md-6 text-center text-md-left"]/text()')

# Extract the text values and append to the scraped_data list
for site in submission_sites:
    scraped_data.append([site.strip()])

# Save the data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(scraped_data)