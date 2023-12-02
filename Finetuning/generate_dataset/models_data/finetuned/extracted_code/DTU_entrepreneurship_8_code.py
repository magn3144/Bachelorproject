
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the header element
header_element = tree.xpath("//h2[contains(text(), 'CENTRE FOR TECHNOLOGY ENTREPRENEURSHIP')]")[0]

# Find the parent element of the header element
parent_element = header_element.getparent()

# Find all paragraph elements within the parent element
paragraph_elements = parent_element.xpath("//p")

# Extract the text from the paragraph elements
description = "\n".join([paragraph_elements[i].text for i in range(len(paragraph_elements))])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Description"])
    writer.writerow([description])
