import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/nasdaq.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find all P and LI elements
p_elements = tree.xpath('//p')
li_elements = tree.xpath('//li')

# Extract the text content from the elements
p_texts = [p.text_content().strip() for p in p_elements]
li_texts = [li.text_content().strip() for li in li_elements]

# Combine the extracted texts
data = p_texts + li_texts

# Save the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Data'])
    writer.writerows([[item] for item in data])