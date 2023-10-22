import csv
from bs4 import BeautifulSoup

# Set the local path to the HTML file
local_path = 'downloaded_pages/washingtonpost.html'

# Load the HTML file
with open(local_path, 'r') as f:
    html = f.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all news article elements
article_elements = soup.find_all('p', class_='wpds-c-kjCVnC')

# Extract the timestamps
timestamps = [element.get_text() for element in article_elements]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp'])
    writer.writerows([[timestamp] for timestamp in timestamps])