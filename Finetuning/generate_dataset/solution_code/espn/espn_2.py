from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/espn.html', 'r') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# Find all the location details
location_details = soup.find_all(class_='LocationDetail__Item')

# Open the CSV file for writing
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the headers
    writer.writerow(['Location'])

    # Write the location details
    for detail in location_details:
        writer.writerow([detail.get_text().strip()])