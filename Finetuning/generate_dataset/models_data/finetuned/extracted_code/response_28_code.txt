import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the element with the release year
release_year_element = tree.xpath("//*[@class='ipc-title__text'][contains(text(), 'Judgment at Nuremberg')]/following::span[@class='ipc-rating-star--rate'][1]/preceding::div[@class='ipc-title__description'][1]/text()")

# Extract the release year
release_year = release_year_element[0].strip()

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Movie', 'Release Year'])
    writer.writerow(['Judgment at Nuremberg', release_year])
