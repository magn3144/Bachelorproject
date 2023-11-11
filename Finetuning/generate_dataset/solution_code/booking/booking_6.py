from bs4 import BeautifulSoup
import csv

# Load HTML file
with open('downloaded_pages/booking.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all property elements
properties = soup.find_all('div', class_='sr_property_block')

# Prepare data list
data = [['Average Rating', 'Number of Reviews']]

# Extract average rating and number of reviews for each property
for property in properties:
    average_rating = property.find('span', class_='average').text.strip()
    num_reviews = property.find('span', class_='review-score-widget__subtext').text.strip()
    
    data.append([average_rating, num_reviews])

# Save data as CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)