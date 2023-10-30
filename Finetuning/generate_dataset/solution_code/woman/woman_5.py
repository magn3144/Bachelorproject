import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/woman.html', 'r', encoding='utf-8') as file:
    html_data = file.read()

# Create an HTML parser
parser = etree.HTMLParser()

# Parse the HTML document
tree = etree.parse(html_data, parser)

# Find all links to podcast episodes
links = tree.xpath('//a[contains(text(), "Podcast")]')

# Extract the href attribute from each link
episode_links = [link.get('href') for link in links]

# Write the episode links to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Podcast Episode Links'])
    writer.writerows([[link] for link in episode_links])