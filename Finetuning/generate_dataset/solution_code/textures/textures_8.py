import csv
from lxml import etree

# Define the target HTML file
html_file = "downloaded_pages/textures.html"

# Define the XPath expressions for the texture format information
xpath_expression = "//div[contains(@class, 'attribute')]"

# Create a list to store the scraped data
scraped_data = []

# Parse the HTML file using lxml
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Extract the texture format information using XPath
texture_formats = tree.xpath(xpath_expression)

# Iterate over the texture formats and extract the relevant data
for format_elem in texture_formats:
    format_info = format_elem.text.strip()
    scraped_data.append(format_info)

# Define the CSV file name
csv_file = "scraped_data.csv"

# Write the scraped data to a CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Texture Formats"])
    writer.writerows(zip(scraped_data))