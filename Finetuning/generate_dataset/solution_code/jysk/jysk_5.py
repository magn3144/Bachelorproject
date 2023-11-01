from bs4 import BeautifulSoup
import csv

# Load the HTML file
with open('downloaded_pages/jysk.html', 'r') as f:
    html_content = f.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find the newsletter subscription description
newsletter_desc = soup.find('p', class_='newsletter-desc').text.strip()

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Newsletter Description'])
    writer.writerow([newsletter_desc])