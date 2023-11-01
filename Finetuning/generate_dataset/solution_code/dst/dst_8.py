from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/dst.html') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the keyword box period information
keyword_box_period = soup.find(class_='keyword_box_period').text.strip()

# Save the keyword box period as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Keyword Box Period'])
    writer.writerow([keyword_box_period])