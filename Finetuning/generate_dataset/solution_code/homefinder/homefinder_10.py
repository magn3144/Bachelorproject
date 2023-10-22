import csv
from bs4 import BeautifulSoup

# Define the HTML file path
html_file = 'downloaded_pages/homefinder.html'

# Create a list to store the scraped data
data = []

# Read the HTML file
with open(html_file, 'r') as file:
    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(file, 'html.parser')
    
    # Find all div elements with class 'listing-ribbon' and text 'Pending'
    pending_listings = soup.find_all('div', class_='listing-ribbon', text='Pending')
    
    # Loop through the pending listings
    for listing in pending_listings:
        # Find the parent div element
        parent_div = listing.parent
        
        # Find the address within the parent div
        address = parent_div.find('div', class_='addr-component').get_text(strip=True)
        
        # Find the real estate agent within the parent div
        agent = parent_div.find('span', class_='cobrand-attribution-line1').get_text(strip=True)
        
        # Add the address and agent to the data list
        data.append([address, agent])

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)