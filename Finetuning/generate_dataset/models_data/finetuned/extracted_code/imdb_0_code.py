
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the elements containing the movie titles and ratings
movie_titles = tree.xpath('//div[@class="ipc-movie-title"]')
movie_ratings = tree.xpath('//span[@class="ipc-rating-star--rating"]')

# Create a list of tuples containing the movie titles and ratings
data = []
for movie_title, movie_rating in zip(movie_titles, movie_ratings):
    data.append((movie_title.text, movie_rating.text))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Movie Title', 'Rating'])
    writer.writerows(data)
