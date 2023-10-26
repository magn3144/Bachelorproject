from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/dice.html', 'r') as file:
    html = file.read()

# Initialize BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all company names
company_names = []
for element in soup.find_all('a', class_='card-title-link bold'):
    company_names.append(element.text.strip())

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name'])
    for name in company_names:
        writer.writerow([name])