from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/bbc_weather.html', 'r') as file:
    html = file.read()

# Parse HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the accessibility links
accessibility_links = soup.find_all('a', text='Accessibility Help')

# Extract title from accessibility links
titles = [link.text for link in accessibility_links]

# Save data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerows([[title] for title in titles])