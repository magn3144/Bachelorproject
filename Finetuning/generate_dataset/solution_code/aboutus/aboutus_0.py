from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open("downloaded_pages/aboutus.html", "r") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all title elements
titles = soup.find_all('title')

# Write the titles to a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for title in titles:
        writer.writerow([title.text])