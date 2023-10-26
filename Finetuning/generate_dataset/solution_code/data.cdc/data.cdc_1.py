from bs4 import BeautifulSoup
import csv

# Load HTML file
with open('downloaded_pages/data.cdc.html', 'r') as file:
    data = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(data, 'html.parser')

# Find all category names
categories = []
category_elements = soup.find_all(class_='browse2-result-category')
for element in category_elements:
    categories.append(element.text.strip())

# Save scraped data as CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for category in categories:
        writer.writerow([category])