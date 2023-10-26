import csv
from lxml import html

# Define the XPaths for the elements
xpaths = {
    'country': '/html/body/div[4]/div[3]/div[1]/div/div/div/ul[2]/li[2]/div/h3/following::span[1]'
}

# Parse the HTML file
with open('downloaded_pages/ebay.html', 'r') as f:
    content = f.read()
tree = html.fromstring(content)

# Extract the text for "Country/Region of Manufacture"
country = tree.xpath(xpaths['country'])

# Save the scraped data as CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Country/Region of Manufacture'])
    writer.writerow([country])