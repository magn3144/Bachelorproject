import csv
from lxml import etree

# Define the target page file path
file_path = 'downloaded_pages/data.cdc.html'

# Define the XPaths for the elements to be scraped
view_count_xpath = '/html/body/div[2]/div/div[6]/div/div[4]/div[2]/div[2]/div[8]/div/div[4]/div[2]/div[2]'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(file_path, parser)

# Extract the view count element
view_count_element = tree.xpath(view_count_xpath)[0]

# Get the view count value
view_count = view_count_element.text.strip()

# Save the view count as CSV
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['View Count'])
    writer.writerow([view_count])