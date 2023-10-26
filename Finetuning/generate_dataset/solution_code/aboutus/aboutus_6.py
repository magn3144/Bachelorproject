from bs4 import BeautifulSoup
import csv

# Open the HTML file
with open('downloaded_pages/aboutus.html', 'r') as file:
    html_data = file.read()

# Parse the HTML
soup = BeautifulSoup(html_data, 'html.parser')

# Find all 'dd' elements
dd_elements = soup.find_all('dd')

# Collect the text content of 'dd' elements
data = [dd.get_text() for dd in dd_elements]

# Save the data in a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Scraped Data'])
    writer.writerows(data)