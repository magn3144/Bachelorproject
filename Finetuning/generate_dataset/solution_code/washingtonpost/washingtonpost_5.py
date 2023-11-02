import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/washingtonpost.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all featured articles and their authors
featured_articles = soup.find_all(class_='wpds-c-fJKSbB wpds-c-fJKSbB-lheJVL-featured-false')
article_authors = soup.find_all(class_='wpds-c-knSWeD wpds-c-knSWeD-iRfhkg-as-a')

# Create a list to store the scraped data
scraped_data = []
for article, author in zip(featured_articles, article_authors):
    scraped_data.append([article.get_text(), author.get_text()])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Article', 'Author'])
    writer.writerows(scraped_data)