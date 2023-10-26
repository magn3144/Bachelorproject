from bs4 import BeautifulSoup
import csv

# Load the HTML file
with open('downloaded_pages/cbsports.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the specific nested elements that contain list items
nested_elements = soup.select('div.grid-view-item__title.product-card__title')

# Extract the text from list items
list_items_text = [element.get_text(strip=True) for element in nested_elements]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['List Items'])
    writer.writerows([[item] for item in list_items_text])