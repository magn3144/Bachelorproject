import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/census.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all elements with class uscb-default-x-column-title and extract the text
titles = [element.text for element in soup.find_all(class_='uscb-default-x-column-title')]

# Find all elements with class uscb-default-x-column-content and extract the text
contents = [element.text for element in soup.find_all(class_='uscb-default-x-column-content')]

# Combine titles and contents into a list of dictionary
data = [{'Title': title, 'Content': content} for title, content in zip(titles, contents)]

# Save the data as CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Title', 'Content'])
    writer.writeheader()
    writer.writerows(data)