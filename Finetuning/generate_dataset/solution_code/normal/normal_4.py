import csv
from lxml import html

# Load the HTML file
path = 'downloaded_pages/normal.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Parse HTML
tree = html.fromstring(content)

# Retrieve all customer testimonials and feedback
testimonials = tree.xpath("//div[contains(@class, 'testimonial')]/p/text()")

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Testimonial'])
    writer.writerows([[testimonial] for testimonial in testimonials])