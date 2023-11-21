import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open('downloaded_pages/4chan.html', 'r') as f:
    html = f.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all board title elements
board_titles = soup.find_all('div', class_='boardTitle')

# Create a list to store the scraped data
data = []

# Extract the board titles and corresponding XPaths
for board_title in board_titles:
    title = board_title.text
    xpath = board_title.xpath('xpath expression here')
    data.append([title, xpath])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)