import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/walmart.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all div elements with class "f7"
addresses = soup.find_all('div', class_='f7')

# Write the addresses to CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Address'])
    for address in addresses:
        writer.writerow([address.text])