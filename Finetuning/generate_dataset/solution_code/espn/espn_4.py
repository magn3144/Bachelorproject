import csv
from bs4 import BeautifulSoup

# HTML file path
html_file_path = 'downloaded_pages/espn.html'

# Parse HTML file
with open(html_file_path, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all news descriptions
news_descriptions = soup.find_all('div', class_='News__Item__Description')

# Save data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['News Descriptions'])
    for description in news_descriptions:
        writer.writerow([description.get_text()])