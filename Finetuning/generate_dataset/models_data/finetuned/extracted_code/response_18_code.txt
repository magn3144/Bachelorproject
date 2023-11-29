
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the Hosting section
hosting_section = tree.xpath('//*[@id="footerHosting"]')

# Extract the text from the section
hosting_text = hosting_section[0].text_content()

# Split the text into lines
hosting_lines = hosting_text.split('\n')

# Remove the empty lines
hosting_lines = [line for line in hosting_lines if line != '']

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Hosting'])
    writer.writerow([hosting_lines])
