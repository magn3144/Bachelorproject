import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/bbc.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Retrieve the most read articles
most_read_articles = []
most_read_elements = tree.xpath('//h2[@id="nw-c-most-read-heading__title"]/following-sibling::ol//span[@class="gs-c-promo-heading__title gel-pica-bold"]')
for element in most_read_elements:
    article_title = element.text.strip()
    most_read_articles.append(article_title)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Most Read Articles'])
    writer.writerows([article] for article in most_read_articles)