import csv
from bs4 import BeautifulSoup

# Open the HTML file and parse it with BeautifulSoup
with open('downloaded_pages/espn.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all the <div> elements that contain the over/under data
over_under_divs = soup.find_all('div', class_='db')

# Extract the over/under values from the <div> elements
over_under_values = [div.get_text().replace('O/U: ', '') for div in over_under_divs]

# Write the over/under values to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Over/Under'])
    writer.writerows([[value] for value in over_under_values])