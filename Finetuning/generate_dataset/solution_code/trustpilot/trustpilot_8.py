import csv
from lxml import etree

# Define the local path to the HTML file
html_file = 'downloaded_pages/trustpilot.html'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Get the recently reviewed businesses
recently_reviewed = tree.xpath('/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/a/div[2]/span/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Business Name'])
    for business in recently_reviewed:
        writer.writerow([business])