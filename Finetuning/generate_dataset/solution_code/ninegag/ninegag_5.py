from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/9gag.html') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all the post elements
posts = soup.find_all('article')

# Initialize a list to store the scraped data
data = []

# Extract the tags/categories for each post
for post in posts:
    tags = post.find_all('a', class_='badge-item-title')
    tags_list = [tag.text.strip() for tag in tags]
    
    if tags_list:
        data.append(tags_list)

# Save the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)