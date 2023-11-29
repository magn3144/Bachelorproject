
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find the elements with the given XPaths
emergency_stays = tree.xpath('//*[@id="footerHeading"]/following-sibling::section/ul/li[6]/a')

# Extract the text from the elements
emergency_stays_text = [e.text for e in emergency_stays]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Emergency Stays'])
    writer.writerow(emergency_stays_text)
