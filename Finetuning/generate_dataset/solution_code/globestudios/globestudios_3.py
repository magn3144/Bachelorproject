import csv
from lxml import etree

# Define the path to the HTML file
path = "downloaded_pages/globestudios.html"

# Define the XPath of the target element
xpath = "/html/body/div/div[3]/div[2]/div/div/div/div/div[1]/div[10]/product-card/div/a"

# Read the HTML file
with open(path, "r", encoding="utf-8") as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find the target element using XPath
element = tree.xpath(xpath)[0]

# Extract the text from the element
text = element.text

# Create and write the scraped data to a CSV file
with open("scraped_data.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([text])