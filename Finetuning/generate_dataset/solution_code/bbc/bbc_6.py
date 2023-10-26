import csv
from lxml import etree

# Load the HTML file
html_file = "downloaded_pages/bbc.html"
with open(html_file, "r", encoding="utf-8") as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find articles about weird aliens in the 19th century
articles = tree.xpath("//h3[contains(@class, 'gs-c-promo-heading__title') and contains(text(), 'weird aliens')]/parent::*/parent::*")

# Extract the titles and save as CSV
data = []
for article in articles:
    title = article.xpath(".//h3[contains(@class, 'gs-c-promo-heading__title')]")[0].text.strip()
    data.append([title])

with open("scraped_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)