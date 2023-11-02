import csv
from urllib.request import urlopen
from lxml import etree

# Open the local HTML file
html = urlopen("file://path/to/downloaded_pages/census.html")

# Parse the HTML content
parser = etree.HTMLParser()
tree = etree.parse(html, parser)

# Find the American Community link
link = tree.xpath("//a[contains(@class, 'uscb-header-panel-content-link') and normalize-space(text())='American Communit']")

# Extract the text of the link
link_text = link[0].text.strip() if link else None

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Link"])
    writer.writerow([link_text])