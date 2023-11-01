import csv
from lxml import html

# Set the path to the HTML file
html_file_path = 'downloaded_pages/textures.html'

# Load the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    page_content = file.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find all texture tags within the category "Digital Websites"
texture_tags = tree.xpath("//div[@class='category' and text()='Digital Websites']/following-sibling::div[@class='texture']/h3/text()")
texture_descs = tree.xpath("//div[@class='category' and text()='Digital Websites']/following-sibling::div[@class='texture']/p/text()")

# Zip the texture tags and descriptions together
texture_data = list(zip(texture_tags, texture_descs))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Texture Tag', 'Description'])
    writer.writerows(texture_data)