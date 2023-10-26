import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/aboutus.html', 'r') as file:
    html_data = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_data, 'html.parser')

# Find all spans in the page
spans = soup.find_all('span')

# Write the spans to CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])

    for span in spans:
        writer.writerow([span.text])