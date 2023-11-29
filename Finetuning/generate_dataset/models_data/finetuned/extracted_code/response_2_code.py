import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the heading element
heading_element = tree.xpath('//*[@id="footerJob"]/h2')

# Extract the text from the heading element
heading_text = heading_element[0].text

# Save the data as a CSV file
data = [heading_text]
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(data)
