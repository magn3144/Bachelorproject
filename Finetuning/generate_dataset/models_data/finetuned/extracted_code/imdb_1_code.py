
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/imdb.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the news articles
news_articles = tree.xpath('//div[@class="news-preview-card-articleTitle"]')

# Extract the descriptions
descriptions = []
for article in news_articles:
    description = article.text_content().strip()
    descriptions.append(description)

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Description'])
    writer.writerows([descriptions])
