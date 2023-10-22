import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/census.html', 'r') as f:
    html = f.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the director's blog post
director_blog = soup.find('p', class_='uscb-footer-text').text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Director Blog'])
    writer.writerow([director_blog])