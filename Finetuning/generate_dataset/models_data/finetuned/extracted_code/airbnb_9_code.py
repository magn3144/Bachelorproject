
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find all the "Guest favorite" divs
guest_favorite_divs = tree.xpath('//div[@class="t1qa5xaj dir dir-ltr"]')

# Find all the location divs
location_divs = tree.xpath('//div[@class="dir dir-ltr"]')

# Create a list of tuples with the location and guest favorite for each Airbnb
data = []
for guest_favorite_div, location_div in zip(guest_favorite_divs, location_divs):
    data.append((location_div.text.strip(), guest_favorite_div.text.strip() == 'Guest favorite'))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Location', 'Guest favorite'])
    writer.writerows(data)
