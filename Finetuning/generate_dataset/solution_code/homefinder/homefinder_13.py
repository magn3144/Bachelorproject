import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open('downloaded_pages/homefinder.html', 'r') as file:
    html = file.read()

# Parse the HTML file
soup = BeautifulSoup(html, 'html.parser')

# Find all the house listings
listings = soup.find_all('div', class_='addr-component')

# Extract the address and real estate agent from each listing and save them as a list of dictionaries
data = []
for listing in listings:
    address = listing.get_text().strip()
    agent = listing.find_next('span', class_='cobrand-attribution-line1').get_text().strip()
    data.append({'Address': address, 'Real Estate Agent': agent})

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Address', 'Real Estate Agent'])
    writer.writeheader()
    writer.writerows(data)