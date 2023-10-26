import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/century21.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all property elements
property_elements = soup.find_all('div', class_='property-card')

# Initialize the data list
data = []

# Iterate over the property elements
for element in property_elements:
    # Find the image count element
    image_count_element = element.find('div', class_='image-count-total')
    
    # Extract the image count
    image_count = image_count_element.text.strip() if image_count_element else 'N/A'
    
    # Append the data to the list
    data.append([image_count])

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)