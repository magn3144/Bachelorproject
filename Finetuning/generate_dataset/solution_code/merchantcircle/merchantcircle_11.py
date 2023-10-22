from bs4 import BeautifulSoup
import csv

# Open the HTML file
with open('downloaded_pages/merchantcircle.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all itemDesc links with class btn-filled
links = soup.find_all('a', class_='btn-filled', text=True)

# Extract the text from the links
data = [link.text for link in links]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Scraped Data'])
    writer.writerows(zip(data))