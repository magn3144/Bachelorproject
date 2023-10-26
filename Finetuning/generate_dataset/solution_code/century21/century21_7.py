import csv
from bs4 import BeautifulSoup

# Open the HTML file and read its contents
with open('downloaded_pages/century21.html', 'r') as f:
    html = f.read()

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all the learning resources on the page
learning_resources = soup.find_all('li', class_='header')

# Create a list to store the scraped data
data = [['Learning Resource']]

# Append each learning resource to the data list
for resource in learning_resources:
    data.append([resource.text.strip()])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)