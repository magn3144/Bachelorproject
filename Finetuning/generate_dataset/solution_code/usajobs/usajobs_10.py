import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/usajobs.html', 'r') as f:
    html = f.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Scrape the jump titles and target XPaths
jump_titles = soup.find_all('h5', class_='usajobs-search-refiner__jump-title')
target_xpaths = soup.find_all('li', class_='usajobs-search-result--core__item')

# Create a dictionary to store the scraped data
data = {}
for title, xpath in zip(jump_titles, target_xpaths):
    data[title.text.strip()] = xpath.text.strip()

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Jump Title', 'Target XPath'])
    for title, xpath in data.items():
        writer.writerow([title, xpath])