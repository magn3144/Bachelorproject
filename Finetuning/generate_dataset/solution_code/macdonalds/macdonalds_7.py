import csv
from lxml import html

# Open the HTML file
with open('downloaded_pages/macdonalds.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find all image elements and extract their source URLs
image_elements = tree.xpath('//img')
image_urls = [element.get('src') for element in image_elements]

# Create a CSV file and write the image URLs
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Image URL'])
    writer.writerows([[url] for url in image_urls])