import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/monstercat.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Scrape the global footer section
section_headers = tree.xpath('//div[@class="global-footer__section-header"]/text()')
content_elements = tree.xpath('//div[@class="global-footer__section-header"]/following-sibling::node()[1]/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Section Header', 'Content'])
    for header, content in zip(section_headers, content_elements):
        writer.writerow([header.strip(), content.strip()])