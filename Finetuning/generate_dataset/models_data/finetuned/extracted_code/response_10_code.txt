
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find all the "Airbnb-friendly apartments"
apartments = tree.xpath('//a[contains(text(), "Airbnb-friendly apartments")]')

# Create the CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Airbnb-friendly apartments'])

    # Loop over all the apartments
    for apartment in apartments:
        # Get the apartment text
        text = apartment.text

        # Write the apartment text to the CSV file
        writer.writerow([text])
