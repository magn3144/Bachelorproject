
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find the "Inspiration for future getaways" header
header = tree.xpath("//h2[contains(text(), 'Inspiration for future getaways')]")[0]

# Find the parent of the header
parent = header.getparent()

# Find the div that contains the "popular" tab
popular_tab = parent.xpath("//div[contains(@class, 'l1f6c880 fy9w785c')]")[0]

# Find the div that contains the locations
locations = popular_tab.xpath("//div[contains(@class, 't1jojoys')]")

# Create a list of tuples with the text and link of each location
data = []
for location in locations:
    text = location.text_content().strip()
    link = location.xpath("a/@href")[0]
    data.append((text, link))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Text', 'Link'])
    writer.writerows(data)
