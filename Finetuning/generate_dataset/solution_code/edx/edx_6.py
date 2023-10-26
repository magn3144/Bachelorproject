from bs4 import BeautifulSoup
import csv

# Open the HTML file
with open('downloaded_pages/edx.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the heading with the text 'EARN YOUR ONLINE GRADUATE DEGREE'
heading = soup.find('h3', text='EARN YOUR ONLINE GRADUATE DEGREE')

# Get the text of the heading
heading_text = heading.get_text()

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Scraped Data'])
    writer.writerow([heading_text])