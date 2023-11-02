from bs4 import BeautifulSoup
import csv

# Open the HTML file
with open('downloaded_pages/merchantcircle.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all addresses and corresponding websites
addresses = []
websites = []

address_elements = soup.find_all('span', class_='street-address')
website_elements = soup.find_all('a', class_='url org')

for element in address_elements:
    addresses.append(element.text.strip())

for element in website_elements:
    websites.append(element['href'])

# Zip the addresses and websites into a list of tuples
data = list(zip(addresses, websites))

# Save the data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Address', 'Website'])
    writer.writerows(data)