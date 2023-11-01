import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/macdonalds.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the legal bumper section
legal_bumper_title = soup.find('h2', class_='cmp-legal-bumper__title').get_text(strip=True)
legal_bumper_description = soup.find('div', class_='cmp-order-delivery-modal__description').get_text(strip=True)

# Create a dictionary with the scraped data
data = {
    'Title': legal_bumper_title,
    'Description': legal_bumper_description
}

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Title', 'Description'])
    writer.writeheader()
    writer.writerow(data)