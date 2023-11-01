import csv
from lxml import etree

# Path to HTML file
html_file = 'downloaded_pages/myspace.html'

# XPath expression for the target element
xpath_expression = '/html/body/div[1]/div[5]/h3'

# Load HTML file
with open(html_file, 'r') as file:
    html_content = file.read()

# Parse HTML
tree = etree.HTML(html_content)

# Find the target element using XPath
target_element = tree.xpath(xpath_expression)[0]

# Extract the text from the target element
text = target_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([text])