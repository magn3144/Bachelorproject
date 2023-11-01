from bs4 import BeautifulSoup
import csv

# Read the local HTML file
with open('downloaded_pages/tripadvisor.html') as file:
    html = file.read()

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find the top-rated restaurants in Vejen
restaurants = soup.find_all('a', class_='cJTqz S4')

# Prepare the data for CSV file
data = [['Restaurant Name']]
for restaurant in restaurants:
    data.append([restaurant.text])

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)