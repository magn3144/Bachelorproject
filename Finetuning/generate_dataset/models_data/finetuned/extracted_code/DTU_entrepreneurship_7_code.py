
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find all the h2 headings
headings = tree.xpath('//h2')

# Create a list of tuples containing the heading text and the corresponding XPath
data = [(heading.text, heading.getroottree().getpath(heading)) for heading in headings]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Heading text', 'XPath'])
    writer.writerows(data)
