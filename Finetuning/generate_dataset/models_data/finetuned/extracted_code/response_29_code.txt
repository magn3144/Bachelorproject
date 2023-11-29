import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the elements with the given XPaths
titles = tree.xpath('//*[@class="ipc-title__text"]')
release_years = tree.xpath('//*[@class="ipc-meta-item__value"]')

# Create a list of tuples with the title and release year
data = list(zip(titles, release_years))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Release Year'])
    writer.writerows(data)
