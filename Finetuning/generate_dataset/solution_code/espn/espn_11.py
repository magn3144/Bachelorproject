import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open('downloaded_pages/espn.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all score network items
score_network_items = soup.find_all(class_='ScoreCell__NetworkItem')

# Extract the text from the score network items
score_networks = [item.get_text(strip=True) for item in score_network_items]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Score Network'])
    writer.writerows(zip(score_networks))