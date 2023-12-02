
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find all the movie release year elements
release_year_elements = tree.xpath('//span[@class="ipc-rating-star--rate"]')

# Create a list to store the scraped data
scraped_data = []

# Iterate over the release year elements
for release_year_element in release_year_elements:
    # Extract the release year from the element
    release_year = release_year_element.text

    # Add the release year to the scraped data list
    scraped_data.append(release_year)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(scraped_data)

# Print the scraped data
print(scraped_data)
