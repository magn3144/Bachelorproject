
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the site footer
footer = tree.xpath('//*[@id="footer"]')

# Extract the text from the site footer
footer_text = footer[0].text_content()

# Split the text by newlines
footer_lines = footer_text.split('\n')

# Create a list of tuples from the lines
data = [line.split(': ') for line in footer_lines]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
