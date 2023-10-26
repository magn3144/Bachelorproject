import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/careerbuilder.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all the links on the webpage
links = soup.find_all('a')

# Extract the link URLs
urls = [link['href'] for link in links]

# Save the extracted URLs to a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['URL'])
    writer.writerows([[url] for url in urls])