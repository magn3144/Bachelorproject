import csv
from bs4 import BeautifulSoup

# HTML file path
html_file_path = 'downloaded_pages/homefinder.html'

# CSS classes
beds_class = 'text-muted'
baths_class = 'text-muted'
sqft_class = 'text-muted'

# Open HTML file
with open(html_file_path, 'r') as file:
    # Create BeautifulSoup object
    soup = BeautifulSoup(file, 'html.parser')

# Find all property details elements
beds_elements = soup.find_all('div', class_=beds_class)
baths_elements = soup.find_all('div', class_=baths_class)
sqft_elements = soup.find_all('div', class_=sqft_class)

# Save scraped data as CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow(['Bedrooms', 'Bathrooms', 'Sqft'])
    # Write property details
    for beds, baths, sqft in zip(beds_elements, baths_elements, sqft_elements):
        writer.writerow([beds.get_text().strip(), baths.get_text().strip(), sqft.get_text().strip()])