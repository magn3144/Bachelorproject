import csv
from lxml import etree

# Define the XPath to select all spans with a certain class
xpath = "//span[@class='visually-hidden']"

# Parse the HTML file
html_file = "downloaded_pages/cbsports.html"
tree = etree.parse(html_file)

# Select all the spans with the given class
spans = tree.xpath(xpath)

# Extract the text from each span
data = [span.text.strip() for span in spans]

# Save the data as a CSV file
output_file = "scraped_data.csv"
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Scraped Data"])
    for item in data:
        writer.writerow([item])