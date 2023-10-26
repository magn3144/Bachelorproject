from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/bestbuy.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all banner titles
banner_titles = soup.find_all(class_='banner-title')

# Prepare data for CSV
data = []
for title in banner_titles:
    data.append([title.text])

# Save data as CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)