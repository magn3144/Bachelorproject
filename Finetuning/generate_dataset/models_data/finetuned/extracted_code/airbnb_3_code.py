
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find all the date elements
date_elements = tree.xpath('//span[@class="dir dir-ltr"]')

# Create a list of dates
dates = []
for date_element in date_elements:
    dates.append(date_element.text)

# Save the dates as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Date'])
    writer.writerows([dates])
