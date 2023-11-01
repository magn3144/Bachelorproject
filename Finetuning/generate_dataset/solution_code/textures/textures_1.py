import csv
from lxml import etree

# Set variables
html_file = 'downloaded_pages/textures.html'
category = 'Digital Websites'
output_file = 'scraped_data.csv'

# Load HTML file
with open(html_file, 'r') as f:
    html = f.read()

# Create XPath selector
selector = etree.HTML(html)

# Find all artist names and portfolios in the specified category
artist_names = selector.xpath("//div[contains(@class, 'category') and contains(text(), '%s')]/following-sibling::div[@class='artist-name']/text()" % category)
portfolios = selector.xpath("//div[contains(@class, 'category') and contains(text(), '%s')]/following-sibling::div[@class='portfolio-link']/a/@href" % category)

# Combine artist names and portfolios into a list of tuples
data = list(zip(artist_names, portfolios))

# Save the data as a CSV file
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Artist Name', 'Portfolio'])
    writer.writerows(data)