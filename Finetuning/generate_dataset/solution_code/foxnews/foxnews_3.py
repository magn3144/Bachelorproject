import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/foxnews.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find all the article elements
articles = tree.xpath('//article')

# Create a list to store the scraped data
data = []
for article in articles:
    # Get the text content of the article
    content = article.text_content().strip()

    # Append the content to the data list
    data.append(content)

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Content'])
    writer.writerows([[content] for content in data])