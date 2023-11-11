import csv
from lxml import html

# Open HTML file
with open('downloaded_pages/booking.html', 'r') as file:
    html_content = file.read()

# Parse HTML content
tree = html.fromstring(html_content)

# Retrieve availability status of each property
availability_elements = tree.xpath("//div[contains(@class, 'sr-hotel__availability')]")
availability_statuses = [element.text_content().strip() for element in availability_elements]

# Save scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Availability Status'])
    writer.writerows([[status] for status in availability_statuses])