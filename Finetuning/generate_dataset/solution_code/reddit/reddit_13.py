import csv
from lxml import etree

# Define the HTML file path
html_path = "downloaded_pages/reddit.html"

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_path, parser)

# Extract all usernames and contributions
usernames = tree.xpath('//a[starts-with(@class, "_1WUTKdOO96akYfbq4CK6z6")]/text()')
contributions = tree.xpath('//div[starts-with(@class, "tbIApBd2DM_drfZQJjIum")]/text()')

# Combine the usernames and contributions into rows
rows = zip(usernames, contributions)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'Contribution'])
    writer.writerows(rows)