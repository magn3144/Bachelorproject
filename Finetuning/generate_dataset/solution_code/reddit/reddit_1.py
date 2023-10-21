import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/reddit.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all comments and timestamps
comments = soup.find_all('p', class_='_1qeIAgB0cPwnLhDF9XSiJM')
timestamps = soup.find_all('a', class_='_3yx4Dn0W3Yunucf5sVJeFU')

# If the number of comments and timestamps is different, ignore the excess
num_comments = len(comments)
num_timestamps = len(timestamps)
min_num = min(num_comments, num_timestamps)

# Create a list to store the scraped data
data = []

# Extract the comment and timestamp text
for i in range(min_num):
    comment = comments[i].text
    timestamp = timestamps[i].text
    data.append([comment, timestamp])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Comment', 'Timestamp'])
    writer.writerows(data)