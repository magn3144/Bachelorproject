import csv
from bs4 import BeautifulSoup

# Open and read file
with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

# Parse HTML
soup = BeautifulSoup(content, 'lxml')

# Find locations and prices
locations = [div.text for div in soup.find_all('div', class_='t1jojoys dir dir-ltr')]
prices = [span.text for span in soup.find_all('span', class_='a8jt5op dir dir-ltr')]

# Prepare data for CSV
data = list(zip(locations, prices))

# Write to CSV
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Location", "Price per Night"])
    writer.writerows(data)