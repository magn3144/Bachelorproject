import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/aliexpress.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the element using the XPath
element = soup.find('dt', text='AliExpress Multi-Language Sites')

# Get the text of the element
text = element.get_text()

# Save the text as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([text])