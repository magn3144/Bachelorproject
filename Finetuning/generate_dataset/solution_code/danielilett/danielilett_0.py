from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/danielilett.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all headings
headings = soup.find_all(['h1', 'h2', 'h3', 'h4'])

# Prepare data for CSV
data = []
for heading in headings:
    xpath = heading.find_previous(xpath=True)
    text = heading.get_text(strip=True)
    data.append([text, xpath])

# Save data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Heading', 'XPath'])
    writer.writerows(data)