import csv
from lxml import etree

# Read the HTML file
with open("downloaded_pages/alibaba.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Find all the pc-search-education-tip_content divs
div_elements = html_tree.xpath("//div[contains(@class, 'pc-search-education-tip_content')]")

# Extract the text content from the divs
text_content = [element.text.strip() for element in div_elements]

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for content in text_content:
        writer.writerow([content])