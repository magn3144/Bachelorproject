import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/arxiv.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the footer link for "contact arXiv"
footer_link = soup.find('a', text='contact arXiv')

# Extract the title of the footer link
title = footer_link['title']

# Save the scraped data as a CSV file
data = [['Title']]
data.append([title])

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)