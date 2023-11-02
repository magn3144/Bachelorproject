import csv
from bs4 import BeautifulSoup

# Load the HTML file
html_file_path = 'downloaded_pages/monstercat.html'
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the Fandom Apps section
fandom_apps_section = soup.find('h3', class_='global-footer__section-header', text='Fandom Apps').parent

# Scrape the app names and descriptions
apps_data = []
for app in fandom_apps_section.find_all('a'):
    app_name = app.text.strip()
    app_description = app.next_sibling.strip()

    apps_data.append([app_name, app_description])

# Save the scraped data as a CSV file
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['App Name', 'App Description'])
    writer.writerows(apps_data)