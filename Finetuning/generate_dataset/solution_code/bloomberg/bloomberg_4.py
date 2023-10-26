import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open('downloaded_pages/bloomberg.html', 'r') as file:
    html = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the articles in the "Technology" category
articles = soup.select('nav li ul li div section article')

# Extract the titles of the articles
titles = [article.select_one('a h3').text for article in articles]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerows([[title] for title in titles])