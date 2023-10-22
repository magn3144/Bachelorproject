import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open('downloaded_pages/census.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all elements with the class 'uscb-default-x-column-title' 
titles = soup.find_all(class_='uscb-default-x-column-title')

# Extract the category of each dataset
categories = [title.get_text(strip=True) for title in titles]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category'])
    writer.writerows(zip(categories))