import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/merchantcircle.html', 'r') as file:
    html_data = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_data, 'html.parser')

# Find all active tags
active_tags = soup.find_all('a', class_='active')

# Extract the text from active tags
active_text = [tag.get_text() for tag in active_tags]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Active Tags'])
    writer.writerows(zip(active_text))