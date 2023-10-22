import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/census.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the element containing the total number of pages
total_pages_element = soup.find('p', class_='uscb-sub-heading-2 uscb-color-primary uscb-margin-TB-5')

# Extract the total number of pages
total_pages = total_pages_element.text.strip().split(' ')[2]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Total Pages'])
    writer.writerow([total_pages])