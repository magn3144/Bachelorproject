import csv
from bs4 import BeautifulSoup

# Read HTML file
with open('downloaded_pages/etsy.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all category filter options
options = soup.find_all(class_='category-filter--tree-item')

# Save options as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category options'])
    for option in options:
        writer.writerow([option.text.strip()])