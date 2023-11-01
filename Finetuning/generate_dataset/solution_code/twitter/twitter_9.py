import csv
from lxml import etree

# Define the XPaths
xpath = "/html/body/noscript/div/p[3]/a[4]"

# Load the HTML file
with open("downloaded_pages/twitter.html", "r", encoding="utf-8") as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Extract the text using the XPath
element = tree.xpath(xpath)[0]
text = element.text

# Save the scraped data as CSV
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Text"])
    writer.writerow(["Social Media", text])