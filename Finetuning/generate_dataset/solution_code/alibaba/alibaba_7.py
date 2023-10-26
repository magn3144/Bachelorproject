import csv
from lxml import etree

# Define the local path to the HTML file
path = "downloaded_pages/alibaba.html"

# Define the XPaths for the content p elements
xpaths = [
    "/html/body/div/p[@class='content']",
    "//div[@class='pc-search-education-tip_content']",
    "//p[@class='cerf-children-after__desc']",
]

# Parse the HTML file using lxml
parser = etree.HTMLParser()
tree = etree.parse(path, parser)

# Extract the text content of the p elements using the XPaths
data = []
for xpath in xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        text = element.text.strip()
        data.append([text])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)