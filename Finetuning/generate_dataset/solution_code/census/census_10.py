import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/census.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all elements with the specified class and text containing 'ACS Supplemental Poverty Measures (SPM) Research'
elements = soup.find_all('div', class_='uscb-default-x-column-title', text='ACS Supplemental Poverty Measures (SPM) Research F')

# Extract the titles and their corresponding years
data = []
for element in elements:
    title = element.get_text()
    year_element = element.find_next_sibling('div', class_='uscb-author-text-wrapper uscb-meta-data-text')
    year = year_element.get_text()
    data.append([title, year])

# Save the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Year'])
    writer.writerows(data)