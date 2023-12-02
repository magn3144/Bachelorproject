
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the age rating for each movie
movie_ratings = tree.xpath('//span[@class="ipc-rating-star--rate"]/../div/span[@class="ipc-rating-star--voteCount"]/text()')

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Age Rating'])
    writer.writerows([[rating] for rating in movie_ratings])
