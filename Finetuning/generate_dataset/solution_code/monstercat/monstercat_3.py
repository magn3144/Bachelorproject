from bs4 import BeautifulSoup
import csv

# Local path to the HTML file
html_file = 'downloaded_pages/monstercat.html'

# Category
category = "Forums and Review Sites"

# Task
task = "Scrape the list of LPs and save their titles as a CSV file."

# Load HTML file
with open(html_file, 'r') as file:
    html = file.read()

# Parse HTML
soup = BeautifulSoup(html, 'html.parser')

# Find LPs
lp_elements = soup.find_all('span', class_='toctext')
lp_titles = [lp.get_text() for lp in lp_elements]

# Save titles as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['LP Title'])
    writer.writerows([[title] for title in lp_titles])