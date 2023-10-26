from bs4 import BeautifulSoup
import csv

# Load the local HTML file
with open('downloaded_pages/bbc_weather.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the element containing the chance of precipitation value using the corresponding XPath
precipitation_element = soup.find('span', class_='wr-time-slot-secondary__chance-of-rain-value')

# Get the chance of precipitation value
precipitation_value = precipitation_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Chance of Precipitation'])
    writer.writerow([precipitation_value])