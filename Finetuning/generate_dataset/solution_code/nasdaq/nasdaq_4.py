import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/nasdaq.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all LABEL elements and extract their text content
labels = soup.find_all('label')
label_texts = [label.get_text(strip=True) for label in labels]

# Write the extracted data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for label_text in label_texts:
        writer.writerow([label_text])