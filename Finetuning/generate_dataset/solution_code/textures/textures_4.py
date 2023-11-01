import csv
from lxml import html

# Read HTML file
with open('downloaded_pages/textures.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create an HTML tree from the HTML content
tree = html.fromstring(html_content)

# Get all texture preview images within the specified category
category = 'Digital Websites'
image_elements = tree.xpath(f"//div[contains(text(), '{category}')]/following-sibling::div//img")

# Extract the image URLs and store them in a list
image_urls = [image.get('src') for image in image_elements]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Image URL'])
    writer.writerows([[url] for url in image_urls])