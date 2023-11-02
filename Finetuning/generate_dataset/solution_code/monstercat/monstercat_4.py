import csv
from bs4 import BeautifulSoup

# Define the XPath expressions for the table elements
table_xpath = "/html/body/div[4]/div[4]/div[3]/aside/div/div[2]/div[2]/div/div/div/div/div/ul/li/div/div[2]/div[1]/h4"
date_xpath = "/html/body/div[4]/div[4]/div[3]/aside/div/div[2]/div[2]/div/div/div/div/div/ul/li/div/div[2]/div[2]"

# Load the HTML file
with open('downloaded_pages/monstercat.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all the table elements
table_elements = soup.select(table_xpath)
date_elements = soup.select(date_xpath)

# Prepare the data to be saved as CSV
data = []
for table_element, date_element in zip(table_elements, date_elements):
    table_text = table_element.get_text(strip=True)
    date_text = date_element.get_text(strip=True)
    row = [table_text, date_text]
    data.append(row)

# Save the data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)