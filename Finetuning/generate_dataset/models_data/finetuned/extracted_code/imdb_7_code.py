
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the movie with the title "Judgment at Nuremberg"
movie_element = tree.xpath("//div[contains(text(), 'Judgment at Nuremberg')]")[0]

# Find the release year span element
release_year_element = movie_element.xpath("//span[contains(@class, 'ipc-rating-star--rate')]")[0]

# Extract the release year
release_year = release_year_element.text.strip()

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([release_year])
