import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/dk.indeed.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the company names
company_names = []
company_elements = soup.find_all('span', class_='companyName')
for element in company_elements:
    company_names.append(element.text.strip())

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name'])
    writer.writerows(zip(company_names))