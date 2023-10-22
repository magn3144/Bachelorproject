import csv
from bs4 import BeautifulSoup

# Parse the HTML file
with open('downloaded_pages/homefinder.html', 'r') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# Find all the HTML elements containing status information
status_elements = soup.find_all(['div', 'span'], text=['New', 'For Sale', 'House For Sale', 'Condo For Sale'])

# Extract the status values
statuses = [element.get_text(strip=True) for element in status_elements]

# Save the extracted data as a CSV file
headers = ['Status']
data = [[status] for status in statuses]

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)