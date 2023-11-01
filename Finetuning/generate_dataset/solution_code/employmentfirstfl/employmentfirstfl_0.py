import csv
from lxml import etree

# Define the file paths
html_path = 'downloaded_pages/employmentfirstfl.html'
csv_path = 'scraped_data.csv'

# Load the HTML file
with open(html_path, 'r') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.parse(html_path, parser)

# Find all the links in the navigation menu
links = tree.xpath("//div[@class='nav-primary']//a")

# Extract the link text and URL
data = []
for link in links:
    text = link.text.strip()
    url = link.attrib['href']
    data.append({'Text': text, 'URL': url})

# Save the data as a CSV file
with open(csv_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Text', 'URL'])
    writer.writeheader()
    writer.writerows(data)