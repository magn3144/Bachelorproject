import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the news articles
news_articles = tree.xpath('//div[@class="news-preview-card-articleTitle"]')

# Extract the descriptions
descriptions = [article.text_content().strip() for article in news_articles]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Description'])
    writer.writerows([[description] for description in descriptions])
