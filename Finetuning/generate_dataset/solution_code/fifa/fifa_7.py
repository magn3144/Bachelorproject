from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/fifa.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all banner elements
banners = soup.find_all('span', class_='carousel_label__3HO5b')

# Store the banner text and details in a list
data = []
for banner in banners:
    data.append(banner.text)

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Banner Text"])
    writer.writerows([[banner] for banner in data])