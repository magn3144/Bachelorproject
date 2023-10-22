import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/washingtonpost.html', 'r') as file:
    html = file.read()

# Create a soup object
soup = BeautifulSoup(html, 'html.parser')

# Find all div tags with class "gray-dark"
div_tags = soup.find_all('div', class_='gray-dark')

# Extract the text from the div tags
texts = [div.text.strip() for div in div_tags]

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for text in texts:
        writer.writerow([text])