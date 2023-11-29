
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the elements with the given XPaths
titles = tree.xpath('//*[@class="ipc-title__text"]')
positions = tree.xpath('//*[@class="ipc-title-ranking__rank"]')

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Position'])
    for title, position in zip(titles, positions):
        writer.writerow([title.text, position.text])
