import csv
from lxml import etree

# Define the HTML file path
html_file_path = 'downloaded_pages/wordpress.html'

# Define the target XPaths
title_xpath = "/html/head/title"

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file_path, parser)

# Extract the title
title_element = tree.xpath(title_xpath)[0]
title = title_element.text

# Save the extracted data as CSV
with open('scraped_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerow([title])