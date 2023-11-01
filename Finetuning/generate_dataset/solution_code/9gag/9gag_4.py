import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/9gag.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all posts
posts = soup.find_all('div', class_='post')

# Create a list to store the scraped data
data = []

# Iterate through each post and extract the number of likes and shares
for post in posts:
    likes = post.find('span', class_='likes').text
    shares = post.find('span', class_='shares').text
    data.append([likes, shares])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Likes', 'Shares'])
    writer.writerows(data)