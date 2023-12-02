
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find all the movie titles
movie_titles = tree.xpath('//div[@class="sc-bb1bba6c-1 ipcpFw news-preview-card-articleTitle"]/text()')

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Movie Title'])
    writer.writerows([[movie_title] for movie_title in movie_titles])
