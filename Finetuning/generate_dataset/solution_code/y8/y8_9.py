import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open('downloaded_pages/y8.html', 'r') as file:
    html = file.read()

# Scrape the description of the website
soup = BeautifulSoup(html, 'html.parser')
description = soup.find('h2', class_='pre-content__description').text.strip()

# Save the scraped data as a CSV file
data = [['Category', 'Description'], ['Video game Websites', description]]
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)