import csv
from lxml import html

# Define the target page, category, and file path
target_page = 'bloomberg'
category = 'Stocks'
file_path = 'downloaded_pages/bloomberg.html'

# Read the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find all article titles in the specified category
articles = tree.xpath("//h3[@class='article-story__eyebrow' and text()='{}']/following-sibling::p[@class='article-story__headline']".format(category))

# Extract the titles
titles = [article.text_content() for article in articles]

# Save the titles as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerows([[title] for title in titles])