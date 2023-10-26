from bs4 import BeautifulSoup
import csv

# Load the HTML file
with open('downloaded_pages/ziprecruiter.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all navigational links on the page
navigational_links = soup.find_all('a')

# Prepare data for CSV file
data = []
for link in navigational_links:
    data.append([link.text.strip(), link['href']])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Link Text', 'URL'])
    writer.writerows(data)