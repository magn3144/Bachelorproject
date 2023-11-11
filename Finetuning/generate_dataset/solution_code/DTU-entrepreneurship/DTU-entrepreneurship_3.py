import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/DTU-entrepreneurship.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the text under the "Newsletter" heading
newsletter_heading = soup.find('h2', text='Newsletter')
newsletter_text = newsletter_heading.next_sibling.strip()

# Save the scraped data as a CSV file
data = [['Category', 'Text'], ['Educational Websites', newsletter_text]]

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)