import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/tripadvisor.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all restaurants with European and Danish cuisine
restaurants = soup.find_all('div', text=['Europæisk, Dansk'])

# Create a list to store the restaurant names
restaurant_names = []

# Extract the restaurant names and add them to the list
for restaurant in restaurants:
    name = restaurant.find_previous('a').text
    restaurant_names.append(name)

# Write the restaurant names to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for name in restaurant_names:
        writer.writerow([name])