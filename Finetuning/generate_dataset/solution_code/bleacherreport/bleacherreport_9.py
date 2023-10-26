import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/bleacherreport.html', 'r') as f:
    html = f.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all team names
team_names = []
team_name_elements = soup.find_all(class_='teamName')
for element in team_name_elements:
    team_names.append(element.text.strip())

# Save the team names as CSV
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Team Names'])
    writer.writerows(zip(team_names))