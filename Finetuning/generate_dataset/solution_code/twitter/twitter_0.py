import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/twitter.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Retrieve the text from the h1 tag
h1_text = soup.select_one('html > body > noscript > div > h1').get_text()

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([h1_text])