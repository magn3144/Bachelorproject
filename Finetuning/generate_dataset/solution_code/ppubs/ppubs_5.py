import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/ppubs.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# Find all the <p> tags
p_tags = tree.xpath('//p')

# Create a list to store the scraped data
data = []

# Iterate through the <p> tags and their corresponding XPaths
for p_tag in p_tags:
    data.append((p_tag.text.strip(), tree.getpath(p_tag)))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Text', 'XPath'])
    writer.writerows(data)