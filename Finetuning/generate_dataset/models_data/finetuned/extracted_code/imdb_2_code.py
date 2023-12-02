
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find all the movie rating elements
rating_elements = tree.xpath('//span[@class="ipc-rating-star--rate"]')

# Find all the movie title elements
title_elements = tree.xpath('//div[@class="sc-bb1bba6c-1 ipcpFw news-preview-card-articleTitle"]')

# Create a list of tuples containing the rating and the movie title
data = [(rating_elements[i].text, title_elements[i].text) for i in range(len(rating_elements))]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Rating', 'Movie'])
    writer.writerows(data)
