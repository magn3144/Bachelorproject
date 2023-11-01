import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/jysk.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find social media links
social_media_links = []
for element in soup.find_all('a'):
    if 'Facebook' in element.text or 'Instagram' in element.text or 'LinkedIn' in element.text:
        social_media_links.append(element['href'])

# Save data to CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Social Media'])
    writer.writerows([[link] for link in social_media_links])