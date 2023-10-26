import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/ebay.html', 'r') as file:
    html_content = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find the element containing "Slovakia"
element = soup.find('span', text='Slovakia - SVK')

# Extract the text
text = element.get_text(strip=True)

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Scraped Text'])
    writer.writerow([text])