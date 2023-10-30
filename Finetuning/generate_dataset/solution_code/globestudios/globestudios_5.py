import csv
from lxml import etree
from pathlib import Path

# Set the local path to the HTML file
html_file = Path("downloaded_pages/globestudios.html")

# Read the HTML file
with open(html_file, "r", encoding="utf-8") as file:
    html_string = file.read()

# Create an element tree from the HTML string
tree = etree.HTML(html_string)

# Define the XPath of the "Tilføj til kurv" element
xpath = "/html/body/div/div[3]/div[2]/div/div/div/div/div[1]/div[4]/product-card/figure/a/quick-view/span"

# Find the "Tilføj til kurv" element using the XPath
element = tree.xpath(xpath)[0]

# Get the text from the element
text = element.text.strip()

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Text"])
    writer.writerow([text])