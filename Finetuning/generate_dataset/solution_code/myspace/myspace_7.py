import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/myspace.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all news articles in the "NEWS" category
news_articles = soup.select('div.category:contains("NEWS")')

# Extract the titles
titles = [article.get_text(strip=True) for article in news_articles]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title'])
    writer.writerows([[title] for title in titles])