import csv
from bs4 import BeautifulSoup

# Define the target file path
file_path = 'downloaded_pages/merchantcircle.html'

# Create a soup object from the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all locality spans
locality_spans = soup.find_all('span', class_='locality')

# Extract the text from the locality spans
localities = [span.get_text(strip=True) for span in locality_spans]

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Localities'])
    writer.writerows(zip(localities))