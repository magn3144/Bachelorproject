import csv
from bs4 import BeautifulSoup

# Open the HTML file and load its content
with open('downloaded_pages/homefinder.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# Find all div elements with class "listing-ribbon-success" to identify condo listings
condo_listings = soup.find_all('div', class_='listing-ribbon-success')

# Create a list to store scraped data
scraped_data = []

# Scrape the address and real estate agent for each condo listing
for listing in condo_listings:
    address = listing.find_previous('div', class_='addr-component').text.strip()
    agent = listing.find_next('span', class_='cobrand-attribution-line1').text.strip()
    scraped_data.append({'Address': address, 'Real Estate Agent': agent})

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csv_file:
    fieldnames = ['Address', 'Real Estate Agent']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)