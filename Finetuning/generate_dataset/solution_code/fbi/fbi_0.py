import csv
from bs4 import BeautifulSoup

# Parse the HTML file
with open('downloaded_pages/fbi.html', 'r') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# Find all the names and links of fugitives
fugitives = soup.find_all('a')

data = []
for fugitive in fugitives:
    name = fugitive.text
    link = fugitive['href']
    data.append([name, link])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Link'])
    writer.writerows(data)