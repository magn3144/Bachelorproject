import csv
from bs4 import BeautifulSoup

# Define the target HTML file
target_html_file = 'downloaded_pages/imdb.html'

# Open target HTML file and parse its content
with open(target_html_file, 'r') as file:
    soup = BeautifulSoup(file, 'lxml')

# Scrape footer links and their corresponding text
footer_links = []
for a in soup.find_all('a', {'class': 'ipc-link ipc-link--baseAlt ipc-link--touch-target ipc-link--inherit-color'}):
    link_text = a.text.strip()
    link_url = a.get('href')
    footer_links.append([link_text, link_url])

# Store the scraped data in a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link_Text', 'URL'])  # Write header
    writer.writerows(footer_links)  # Write all scraped links