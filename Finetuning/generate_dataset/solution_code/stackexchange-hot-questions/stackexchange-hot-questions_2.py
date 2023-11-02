import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/stackexchange-hot-questions.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the warning message for websites that work best with JavaScript enabled
warning_message = soup.find('div', id='noscript-warning').text

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Warning Message'])
    writer.writerow([warning_message])