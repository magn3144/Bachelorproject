import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open('downloaded_pages/census.html', 'r') as file:
    html_data = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_data, 'html.parser')

# Find the title of the page
title = soup.title.string

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title'])
    writer.writerow([title])