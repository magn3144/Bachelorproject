import csv
from lxml import etree

# Parse the HTML document
parser = etree.HTMLParser()
tree = etree.parse('downloaded_pages/bloomberg.html', parser)

# Get the authors mentioned on the page
authors = tree.xpath('//span[text()="Suzanne Woolley and Claire Ballentine"]/text()')

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Authors'])
    writer.writerows([[author] for author in authors])