import csv
from bs4 import BeautifulSoup
import requests

# Define the local path to the HTML file
html_file_path = 'downloaded_pages/airbnb.html'

# Define the URL and category
url = 'https://www.airbnb.com'
category = 'Tourism'

# Define the XPath expressions for the required information
hosting_xpath = '/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/h3'
csv_data = [['Category', 'Hosting']]

# Retrieve the HTML from the local file
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the required information using XPath
hosting_element = soup.find('h3', class_='trsc28b dir dir-ltr')
hosting = hosting_element.text if hosting_element else None

# Append the scraped data to the CSV data
csv_data.append([category, hosting])

# Save the CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)