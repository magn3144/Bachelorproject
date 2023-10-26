from bs4 import BeautifulSoup
import csv

# Load the HTML file
with open('downloaded_pages/century21.html', 'r') as f:
    html = f.read()

# Parse HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all language elements
language_elements = soup.find_all('a')
languages = [element.string for element in language_elements]

# Save data to CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Language'])
    writer.writerows([[language] for language in languages])