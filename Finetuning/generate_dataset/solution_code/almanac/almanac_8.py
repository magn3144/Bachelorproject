import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/almanac.html', 'r') as file:
    html = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the Where to Buy section
where_to_buy_section = soup.find('a', text='Where to Buy').parent.parent

# Find all the products on sale in the Where to Buy section
products = where_to_buy_section.find_all('p', class_='prod-title')
prices = where_to_buy_section.find_all('p')

# Create a list to store the scraped data
scraped_data = []

# Iterate over the products and prices
for product, price in zip(products, prices):
    name = product.get_text(strip=True)
    price = price.get_text(strip=True)
    scraped_data.append([name, price])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price'])
    writer.writerows(scraped_data)