import csv
from lxml import etree

# Define the file paths
html_file_path = 'downloaded_pages/woman.html'
csv_file_path = 'scraped_data.csv'

# Read the HTML file
with open(html_file_path, 'r') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Get all the links to individual blog posts
links = tree.xpath('//a')

# Extract the href attribute value for each link
link_urls = [link.get('href') for link in links]

# Filter out links that are None or empty
filtered_links = [link for link in link_urls if link is not None and link.strip()]

# Write the links to the CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(filtered_links)