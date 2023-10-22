import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/espn.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all Quick Links titles
quick_links = soup.find_all(class_='QuickLinks__Item__Title')

# Create a list to store the titles
titles = []
for link in quick_links:
    titles.append(link.text)

# Save the titles as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerows(zip(titles))