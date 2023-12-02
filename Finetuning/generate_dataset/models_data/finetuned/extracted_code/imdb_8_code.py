
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find all the footer links
footer_links = tree.xpath('//footer/div[3]/div[1]/div[3]/ul/li/a')

# Create a list of tuples containing the link text and the corresponding URL
data = [(link.text, link.attrib['href']) for link in footer_links]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Link Text', 'URL'])
    writer.writerows(data)
