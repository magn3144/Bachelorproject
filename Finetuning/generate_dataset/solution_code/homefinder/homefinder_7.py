import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/homefinder.html') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all the elements containing phone numbers
phone_elements = soup.find_all('p', class_='phone-action')

# Extract the phone numbers
phone_numbers = [element.get_text(strip=True) for element in phone_elements]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Phone Number'])
    writer.writerows([[number] for number in phone_numbers])