import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/alibaba.html', 'r') as f:
    html = f.read()

# Parse the HTML
tree = etree.HTML(html)

# Find the lfs-filter-wrapper__title-content h5 elements
elements = tree.xpath('//h5[@class="lfs-filter-wrapper__title-content"]')

# Extract the text from the elements
titles = [element.text.strip() for element in elements]

# Save the data as CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerows([[title] for title in titles])