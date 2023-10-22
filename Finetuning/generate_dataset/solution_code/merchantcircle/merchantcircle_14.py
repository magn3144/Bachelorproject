import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/merchantcircle.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all itemDesc links with class btn-filled
links = soup.find_all('a', class_='itemDesc btn-filled')

# Extract the text from the links
data = [link.get_text(strip=True) for link in links]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Scraped Data'])
    writer.writerows([[item] for item in data])