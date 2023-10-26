import csv
from lxml import html

# Open the HTML file
with open('downloaded_pages/bbc.html', 'r') as file:
    page_content = file.read()

# Parse the HTML content
tree = html.fromstring(page_content)

# Find all BBC Culture articles
articles = tree.xpath('//a[contains(@class, "qa-heading-link")]')

# Extract the titles of the articles
titles = [article.text for article in articles]

# Write the titles to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerows([[title] for title in titles])