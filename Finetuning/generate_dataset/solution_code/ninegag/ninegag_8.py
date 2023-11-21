import csv
from bs4 import BeautifulSoup

# Load the HTML file
html_file = 'downloaded_pages/9gag.html'
with open(html_file, 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all posts in the HTML
posts = soup.find_all('article', class_='post')

# Create a list to store the scraped data
data = [['Title', 'Upvotes', 'Downvotes']]

# Iterate over each post and extract the relevant information
for post in posts:
    # Extract the post title
    title = post.find('a', class_='badge-item-title').text.strip()

    # Extract the number of upvotes and downvotes
    score = post.find('div', class_='vote').text
    upvotes, downvotes = score.split('/')

    # Append the data to the list
    data.append([title, upvotes.strip(), downvotes.strip()])

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)