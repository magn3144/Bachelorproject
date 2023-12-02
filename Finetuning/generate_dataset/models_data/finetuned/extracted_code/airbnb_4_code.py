
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

# Iterate over the listings
for listing in listings:
    # Find the location and price of each listing
    location = listing.xpath('.//span[@class="u17llcap dir dir-ltr"]')[0].text.strip()
    price = listing.xpath('.//span[@class="a8jt5op dir dir-lftn"]')[0].text.strip()

    # Save the data to the scraped_data list
    scraped_data.append([location, price])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Location', 'Price'])
    writer.writerows(scraped_data)

# Print the scraped data
print(scraped_data)

