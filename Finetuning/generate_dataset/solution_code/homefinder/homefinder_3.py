from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/homefinder.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all the anchor tags with class 'search-internal-link'
neighborhood_links = soup.find_all('a', class_='search-internal-link')

# Extract the neighborhood names from the anchor tags
neighborhood_names = [link.text.strip() for link in neighborhood_links]

# Save the neighborhood names as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([name] for name in neighborhood_names)