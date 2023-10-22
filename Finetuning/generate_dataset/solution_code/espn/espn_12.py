import csv
from bs4 import BeautifulSoup

# Parse the HTML file
with open('downloaded_pages/espn.html', 'r') as file:
    html = file.read()
soup = BeautifulSoup(html, 'html.parser')

# Extract the field locations
field_locations = []

location_elements = soup.find_all(class_='LocationDetail__Item')
for element in location_elements:
    field_location = element.get_text(strip=True)
    field_locations.append(field_location)

# Save the field locations as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for field_location in field_locations:
        writer.writerow([field_location])