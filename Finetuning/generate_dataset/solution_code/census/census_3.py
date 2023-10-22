import csv
from bs4 import BeautifulSoup

# Load HTML file
html_file = 'downloaded_pages/census.html'
with open(html_file, 'r') as file:
    html = file.read()

# Parse HTML
soup = BeautifulSoup(html, 'html.parser')

# Find last modified date
last_modified = soup.find(id='uscb-automation-lastmodified-date').text

# Write data to CSV file
data = [['Last Modified']]
data.append([last_modified])

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)