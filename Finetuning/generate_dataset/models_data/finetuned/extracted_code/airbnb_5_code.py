
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

# Loop through the listings
for listing in listings:
    # Get the location and link
    location = listing.xpath('.//span[@class="u17llcap"]')[0].text.strip()
    link = listing.xpath('.//a[@class="_14n5tp8o"]/@href')[0]

    # Save the data
    scraped_data.append([location, link])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Location', 'Link'])
    writer.writerows(scraped_data)

# Print the scraped data
print(scraped_data)

