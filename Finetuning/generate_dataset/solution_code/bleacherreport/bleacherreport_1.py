import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/bleacherreport.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Get the date elements
date_elements = tree.xpath('//div[@class="title"]/text()')

# Create a list of dictionaries to store the scraped data
scraped_data = []
for element in date_elements:
    scraped_data.append({'Date': element})

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    fieldnames = ['Date']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)