import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/wikipedia.html', 'r') as html_file:
    # Parse the HTML content
    tree = etree.parse(html_file)

# Find all language options using xpath
language_elements = tree.xpath("//a[contains(@class, 'interlanguage-link-target')]")

# Extract language names and URLs
language_data = []
for element in language_elements:
    language_name = element.text
    language_url = element.get('href')
    language_data.append([language_name, language_url])

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Language', 'URL'])
    writer.writerows(language_data)