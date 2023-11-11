import os
import csv
from bs4 import BeautifulSoup

# Define the local path to the HTML file
html_file = 'downloaded_pages/DTU-entrepreneurship.html'

# Define the target HTML element XPath
target_xpath = '/html/body/form/div[3]/footer/div[3]/div[2]'

# Load the HTML file
with open(html_file, 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the target element using XPath
target_element = soup.find('div', class_='grid_3 pagefootercolumn inline-block minHeight')

# Extract the text from the target element
scraped_text = target_element.get_text().strip()

# Create the CSV file and write the scraped data
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([scraped_text])