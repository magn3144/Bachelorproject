import csv
from bs4 import BeautifulSoup

# Open the HTML file and read its content
with open('downloaded_pages/bestbuy.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all headers of the footer navigation details
footer_headers = soup.select('footer div h3')

# Prepare the data to be saved in the CSV file
data = []
for header in footer_headers:
    data.append([header.text])

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)