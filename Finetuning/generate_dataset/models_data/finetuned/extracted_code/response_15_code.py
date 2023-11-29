
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find all the guest favorite elements
guest_favorites = tree.xpath('//div[@class="t1jojoys dir dir-ltr"]')

# Create a list to store the scraped data
scraped_data = []

# Loop over the guest favorite elements
for guest_favorite in guest_favorites:
    # Extract the title of the guest favorite
    title = guest_favorite.text.strip()

    # Extract the link to the guest favorite
    link = guest_favorite.get('id')

    # Create a dictionary with the scraped data
    data = {
        'Title': title,
        'Link': link
    }

    # Add the data to the list
    scraped_data.append(data)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Title', 'Link'])
    writer.writeheader()
    writer.writerows(scraped_data)
