
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Get the positions of the movies
positions = tree.xpath('//div[@class="ipc-title__description"]/text()')

# Get the movie titles
titles = tree.xpath('//div[@class="ipc-title__text"]/text()')

# Get the release years
years = tree.xpath('//span[@class="ipc-rating-star--rate"]/text()')

# Get the ratings
ratings = tree.xpath('//span[@class="ipc-rating-star--voteCount"]/text()')

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Position', 'Title', 'Year', 'Rating'])
    for position, title, year, rating in zip(positions, titles, years, ratings):
        writer.writerow([position, title, year, rating])
