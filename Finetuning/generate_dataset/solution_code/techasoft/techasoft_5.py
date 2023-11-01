import csv
from lxml import etree

# XPath of the digital marketing services links
links_xpath = "//a[contains(text(),'Digital Marketing')]"

# XPath of the digital marketing services names
names_xpath = "//a[contains(text(),'Digital Marketing')]/text()"

# Load the HTML file
with open('downloaded_pages/techasoft.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create an ElementTree object from the HTML content
tree = etree.HTML(html_content)

# Extract the digital marketing services links
links = tree.xpath(links_xpath)

# Extract the digital marketing services names
names = tree.xpath(names_xpath)

# Combine the names and links into a list
data = list(zip(names, links))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Link'])  # Write the headers
    for row in data:
        writer.writerow(row)