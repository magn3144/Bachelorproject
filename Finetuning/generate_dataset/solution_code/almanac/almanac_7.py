import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/almanac.html', 'r') as f:
    html = f.read()
    
# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all the elements containing names and prices of selected items
name_elements = soup.find_all('p', class_='prod-title')
price_elements = soup.find_all('p')

# Extract the names and prices
names = [element.get_text() for element in name_elements]
prices = [element.get_text() for element in price_elements if element.get_text().startswith('$')]

# Combine names and prices into a list of tuples
data = list(zip(names, prices))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Price'])
    writer.writerows(data)