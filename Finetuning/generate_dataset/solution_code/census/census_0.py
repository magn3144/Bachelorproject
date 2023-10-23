import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/census.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all elements with class 'uscb-default-x-column-title'
titles = soup.find_all(class_='uscb-default-x-column-title')

# Find all elements with class 'uscb-author-text-wrapper'
years = soup.find_all(class_='uscb-author-text-wrapper')

# Create a list to store the scraped data
data = []

# Iterate over the titles and years to extract the text
for title, year in zip(titles, years):
    # Extract the text from the title and year elements
    title_text = title.get_text(strip=True)
    year_text = year.get_text(strip=True)
    
    # Append the data to the list
    data.append([title_text, year_text])

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Year'])
    writer.writerows(data)