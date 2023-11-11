from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/booking.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the 'Unpacked: Travel articles' section
section = soup.find('a', text='Unpacked: Travel articles').parent.parent.next_sibling

# Extract the names and descriptions of the featured articles
articles = section.find_all('li', recursive=False)
data = []
for article in articles:
    name = article.h3.text.strip()
    description = article.p.text.strip()
    data.append([name, description])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)