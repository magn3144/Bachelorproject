import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/homefinder.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all the neighborhoods in New York, NY
neighborhoods = []
for element in soup.find_all('a', class_='search-internal-link d-block'):
    if 'Homes for Sale' in element.text:
        neighborhoods.append(element.text.strip())

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Neighborhood'])
    for neighborhood in neighborhoods:
        writer.writerow([neighborhood])