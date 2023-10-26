import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open("downloaded_pages/aboutus.html") as file:
    html = file.read()

# Initialize the BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Find all 'div' elements
div_elements = soup.find_all("div")

# Prepare the data for CSV
data = []
for div in div_elements:
    data.append([div.get_text()])

# Save the data to CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)