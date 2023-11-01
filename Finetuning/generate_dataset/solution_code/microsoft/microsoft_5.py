import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/microsoft.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all sections under the "Udforsk" header
sections = tree.xpath('//h2[contains(text(),"Udforsk")]/following-sibling::*/section')

# Extract the text content of each section
text_content = []
for section in sections:
    section_text = section.xpath('.//text()')
    text_content.append(section_text)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(text_content)