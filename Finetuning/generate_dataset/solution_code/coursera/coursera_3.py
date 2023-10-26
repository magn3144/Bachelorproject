from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/coursera.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <p> tags
p_tags = soup.find_all('p', class_='cds-119 cds-121')

# Extract duration and specialization information
scraped_data = []
for p in p_tags:
    data = p.get_text()
    scraped_data.append(data.split('·'))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(scraped_data)