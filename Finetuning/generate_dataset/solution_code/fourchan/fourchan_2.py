import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/4chan.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find all date elements using XPath
date_elements = tree.xpath('//td[contains(@class, "blotter-date")]')

# Extract the dates
dates = [date_element.text_content() for date_element in date_elements]

# Save the dates as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date'])
    writer.writerows([[date] for date in dates])