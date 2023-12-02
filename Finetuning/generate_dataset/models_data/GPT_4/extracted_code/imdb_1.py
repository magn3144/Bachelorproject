import csv
import lxml.html as lh

def extract_year(movie):
    try:
        # Extract the release year from the movie title
        return movie[movie.rindex("(") + 1:movie.rindex(")")]
    except ValueError:
        # If no year is found, return None
        return None

# Load the webpage into lxml
with open('downloaded_pages/imdb.html', 'r') as f:
    tree = lh.fromstring(f.read())

# Find all movie titles on the page
movies = tree.xpath('//div[@class="lister-item mode-detail"]/div[2]/h3/a/text()')

# Extract the release years
release_years = [extract_year(movie) for movie in movies]

# Save the data into a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Movie', 'Release Year'])
    for movie, release_year in zip(movies, release_years):
        writer.writerow([movie, release_year])