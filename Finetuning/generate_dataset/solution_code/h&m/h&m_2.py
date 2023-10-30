import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open('downloaded_pages/h&m.html', 'r') as file:
    html = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the title element with id "instagram-logo"
title_element = soup.find(id='instagram-logo')

# Get the text content of the title element
title_text = title_element.get_text()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerow([title_text])