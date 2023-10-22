import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open('downloaded_pages/washingtonpost.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all li tags with the specified class
li_tags = soup.find_all('li', class_='wpds-c-cFhpZV wpds-c-cFhpZV-kEJnWT-mbSm-true')

# Extract the text from the li tags
text_data = [li.get_text(strip=True) for li in li_tags]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])
    writer.writerows([[data] for data in text_data])