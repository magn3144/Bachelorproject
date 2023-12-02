
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find all the airbnb listings
listings = tree.xpath('//div[@class="_14n5tp8o"]')

# Extract the location and stars for each listing
data = []
for listing in listings:
    location = listing.xpath('.//span[@class="u17llcap"]')[0].text.strip()
    stars = listing.xpath('.//div[@class="_14n5tp8o"]//div[@class="t1ja0i6n"]//span[@class="x4ii4kep"]/text()')[0]
    data.append((location, stars))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Location', 'Stars'])
    writer.writerows(data)
