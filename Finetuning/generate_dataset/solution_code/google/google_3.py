import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/google.html', 'r') as file:
    html_data = file.read()

# Create an ElementTree from the HTML data
tree = html.fromstring(html_data)

# Find the element with the heading "This Doodle's Reach"
date_element = tree.xpath('/html/body/div[2]/div/ul/li[3]/h3')[0]

# Extract the date text
date = date_element.text.strip()

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Date'])
    writer.writerow(['Educational Websites', date])