import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open('downloaded_pages/amazon.html', 'r') as file:
    html = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all gaming keyboard elements
keyboard_elements = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')

# Extract brand names and customer ratings
data = []
for element in keyboard_elements:
    brand = element.get_text().strip().split()[0]
    rating = element.find_next('span', class_='a-icon-alt').get_text().split()[0]
    data.append([brand, rating])

# Save the data as a CSV file
with open('keyboard_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Brand', 'Rating'])
    writer.writerows(data)