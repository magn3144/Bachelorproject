import csv
from lxml import etree

# Open and read the HTML file
with open('downloaded_pages/arxiv.html', 'r') as file:
    html_source = file.read()

# Parse the HTML
tree = etree.HTML(html_source)

# Find all authors using XPath
authors = tree.xpath('//div[@class="meta"]/div/a/text()')

# Save the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Authors'])
    writer.writerows(zip(authors))