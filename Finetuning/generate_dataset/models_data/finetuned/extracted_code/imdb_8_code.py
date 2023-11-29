
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the elements with the given XPaths
titles = tree.xpath('//*[@class="ipc-title__text"]')
release_years = tree.xpath('//*[@class="ipc-meta-item__value"]')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Release Year'])
    for title, release_year in zip(titles, release_years):
        writer.writerow([title.text, release_year.text])
