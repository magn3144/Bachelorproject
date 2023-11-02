import csv
from lxml import etree

# Read the HTML file
tree = etree.parse("downloaded_pages/homefinder.html")

# Find the element containing the number of homes for sale
num_homes_element = tree.xpath("//a[contains(@class, 'search-internal-link') and contains(text(), '10011')]")
if num_homes_element:
    num_homes = num_homes_element[0].text.strip()
else:
    num_homes = "N/A"

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Number of Homes for Sale'])
    writer.writerow([num_homes])