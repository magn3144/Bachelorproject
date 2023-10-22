import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/espn.html', 'r') as file:
    html_data = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_data, 'html.parser')

# Find all the elements with timestamp data
timestamps = soup.find_all(class_="MetaContent__Item__Timestamp")

# Extract the timestamp text
timestamp_data = [timestamp.get_text() for timestamp in timestamps]

# Write the timestamp data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp'])
    writer.writerows([[timestamp] for timestamp in timestamp_data])