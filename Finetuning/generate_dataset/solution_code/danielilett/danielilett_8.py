import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/danielilett.html', 'r') as f:
    html_content = f.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all social media links
social_media_links = soup.find_all('span', class_='sr-only')

# Create a list to store the scraped data
scraped_data = []

# Append each link and its XPath to the scraped data list
for link in social_media_links:
    xpath = soup.find_all(text=link)[0].parent.parent.xpath('')[0]
    scraped_data.append([link.text, xpath])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(scraped_data)