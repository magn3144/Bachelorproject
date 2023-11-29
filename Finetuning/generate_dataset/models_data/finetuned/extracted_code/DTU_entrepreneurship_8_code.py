
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the paragraph with the given XPath
paragraph = tree.xpath('//*[@id="outercontent_0_ContentHeading"]/following::p[1]')[0]

# Extract the text from the paragraph
text = paragraph.text_content()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([text])
