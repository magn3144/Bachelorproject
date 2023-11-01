import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/9gag.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find all post images on the homepage
post_images = tree.xpath('//img[contains(@class, "badge-item-img")]')

# Extract the image URLs
image_urls = [image.attrib['src'] for image in post_images]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Image URL'])
    for url in image_urls:
        writer.writerow([url])