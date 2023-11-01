import csv
from lxml import etree

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse('downloaded_pages/top.html', parser)

# Find the <h4> elements using XPath
h4_elements = tree.xpath('//h4')

# Extract the text from each <h4> element
texts = [h4_element.text for h4_element in h4_elements]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Text'])
    writer.writerows([[text] for text in texts])