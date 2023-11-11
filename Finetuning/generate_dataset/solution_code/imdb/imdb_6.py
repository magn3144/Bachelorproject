import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the range of movies
start_movie = soup.find('h3', text='154. Finding Nemo')
end_movie = soup.find('h3', text='228. Pirates of the Caribbean: The Curse of the Black Pearl')

# Scrape the titles and positions of the movies
movies = []
next_movie = start_movie.find_next('h3')
while next_movie != end_movie:
    position = next_movie.text.split('.')[0].strip()
    title = next_movie.text.split('.')[1].strip()
    movies.append({'Position': position, 'Title': title})
    next_movie = next_movie.find_next('h3')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Position', 'Title']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(movies)