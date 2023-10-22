from bs4 import BeautifulSoup
import csv

# Open the HTML file
with open('downloaded_pages/espn.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all stat labels using relevant HTML elements
stat_labels = soup.find_all(class_='Athlete__Stats--label') + soup.find_all(class_='n10 clr-gray-03')

# Save the stat labels as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Stat Label'])
    for label in stat_labels:
        writer.writerow([label.text])