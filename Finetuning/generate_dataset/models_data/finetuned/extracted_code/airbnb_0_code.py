
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find the footer section
footer_section = tree.xpath('//footer/div/div/div/div/section')

# Find the links in the footer section
links = footer_section[0].xpath('//a')

# Extract the link texts and URLs
link_texts = [link.text for link in links]
link_urls = [link.get('href') for link in links]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Link text', 'URL'])
    writer.writerows(zip(link_texts, link_urls))
