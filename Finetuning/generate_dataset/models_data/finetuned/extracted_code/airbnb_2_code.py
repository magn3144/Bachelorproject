
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find all the Airbnb listings
listings = tree.xpath('//div[@class="_14n5tp8o"]')

# Create a list to store the scraped data
scraped_data = []

# Loop through all the listings
for listing in listings:
    # Find the location and distance of the listing
    location = listing.xpath('.//span[@class="u17llcap"]/text()')
    distance = listing.xpath('.//span[@class="_je5epmr8"]/text()')

    # Save the scraped data
    scraped_data.append([location, distance])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Location', 'Distance'])
    writer.writerows(scraped_data)

# Print the scraped data
print(scraped_data)

