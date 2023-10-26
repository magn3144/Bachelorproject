import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/bodybuilding.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Scrape the footer links and their corresponding XPaths
footer_links = tree.xpath('/html/body/footer//a[contains(@href, "http") or contains(@href, "/")]')
footer_xpaths = tree.xpath('/html/body/footer//a[contains(@href, "http") or contains(@href, "/")]/ancestor-or-self::*/@xpath')

# Prepare the data for CSV
data = []
for link, xpath in zip(footer_links, footer_xpaths):
    data.append({'Link': link.text_content().strip(), 'XPath': xpath})

# Save the data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    fieldnames = ['Link', 'XPath']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)