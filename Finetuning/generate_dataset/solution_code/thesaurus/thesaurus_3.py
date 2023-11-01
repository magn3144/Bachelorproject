import csv
from datetime import datetime
from lxml import etree

# Read the HTML file
with open('downloaded_pages/thesaurus.html', 'r') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Find the trending articles and publication dates
articles = tree.xpath("//div[@class='Vmn3EDTx8gXJ1BOikE9Q']")
publication_dates = tree.xpath("//div[@class='Vmn3EDTx8gXJ1BOikE9Q']/span")

# Clean the data
trending_articles = [article.text.strip() for article in articles]
pub_dates = [datetime.strptime(date.text.strip(), "%B %d, %Y") for date in publication_dates]

# Zip the data
data = zip(trending_articles, pub_dates)

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Article', 'Publication Date'])
    writer.writerows(data)