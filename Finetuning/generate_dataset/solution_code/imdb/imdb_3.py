import csv
from lxml import html
from bs4 import BeautifulSoup

# Load the page
with open("downloaded_pages/imdb.html", "r") as f:
    page = f.read()

# Parse the page with BeautifulSoup
soup = BeautifulSoup(page, 'lxml')

# Find the movie duration elements by their class
duration_elements = soup.find_all('span', {'class': 'sc-c7e5f54-8 fiTXuB cli-title-metadata-item'})

# Extract the durations and movie titles, then store them in a list of dictionaries
data = [{'movie': elem.find_previous('h3', {'class': 'ipc-title__text'}).text, 'duration': elem.text} for elem in duration_elements]

# Write the list of dictionaries to a CSV file
with open('scraped_data.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['movie', 'duration'])
    writer.writeheader()
    writer.writerows(data)