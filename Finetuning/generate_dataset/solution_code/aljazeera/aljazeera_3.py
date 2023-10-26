import csv
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/aljazeera.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all hyperlinked text
hyperlinks = soup.find_all('a')

# Extract the text and URL for each hyperlink
data = []
for hyperlink in hyperlinks:
    text = hyperlink.get_text()
    url = hyperlink.get('href')
    absolute_url = urljoin('https://www.aljazeera.com/', url)  # Assumes the base URL is 'https://www.aljazeera.com/'
    data.append([text, absolute_url])

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Text', 'URL'])
    writer.writerows(data)