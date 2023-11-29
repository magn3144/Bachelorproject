
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the elements containing the release years
release_years = tree.xpath('//span[@class="fiTXuB cli-title-metadata-item"]')

# Extract the release years
release_years = [release_year.text for release_year in release_years]

# Save the release years as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Release Year'])
    writer.writerows([release_years])
