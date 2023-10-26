import csv
from lxml import etree

# Parse HTML file
tree = etree.parse('downloaded_pages/data.cdc.html')

# Define namespace
ns = {'html': 'http://www.w3.org/1999/xhtml'}

# Find all MMWR article links using XPath
mmwr_links = tree.xpath(
    '//html:a[starts-with(@href, "http://www.cdc.gov/mmwr/preview/mmwrhtml/")]', namespaces=ns
)

# Extract MMWR articles
articles = []
for link in mmwr_links:
    article = link.text.strip()
    articles.append(article)

# Save scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Article'])
    for article in articles:
        writer.writerow([article])