
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the elements with the given XPaths
movies = tree.xpath('//*[@id="apocalypse-now-to-witness-for-the-prosecution-range"]/div/ul/li/div[2]/div/div/div[1]/a/h3/text()')
positions = tree.xpath('//*[@id="apocalypse-now-to-witness-for-the-prosecution-range"]/div/ul/li/div[2]/div/div/div[1]/a/span/span/span/text()')

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Movie', 'Position'])
    for movie, position in zip(movies, positions):
        writer.writerow([movie, position])
