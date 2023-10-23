import csv
from bs4 import BeautifulSoup

# Parse the HTML file
with open('downloaded_pages/espn.html', 'r') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# Find all gamecast links
gamecast_links = soup.find_all('a', class_='AnchorLink MatchInfo__Link')

# Save the links as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Gamecast Links'])

    for link in gamecast_links:
        writer.writerow([link.get('href')])