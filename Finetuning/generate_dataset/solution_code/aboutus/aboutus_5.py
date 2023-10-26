from bs4 import BeautifulSoup
import csv

# Load the HTML file
with open('downloaded_pages/aboutus.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all paragraph tags
paragraphs = soup.find_all('p')

# Extract the text from each paragraph and store in a list
data = [p.get_text(strip=True) for p in paragraphs]

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Paragraph Text'])
    writer.writerows(data)