import csv
from lxml import etree

# Define the HTML file path
html_file_path = 'downloaded_pages/textures.html'

# Define the XPaths for the relevant elements
rating_xpath = '//div[@class="texture-rating"]/span[@class="rating-value"]'
comment_xpath = '//div[@class="feedback-comment"]/p'

# Create an empty list to store the scraped data
scraped_data = []

# Parse the HTML file
tree = etree.parse(html_file_path)

# Extract all texture ratings
ratings = tree.xpath(rating_xpath)
for rating in ratings:
    scraped_data.append((rating.text.strip(),))

# Extract all feedback comments
comments = tree.xpath(comment_xpath)
for comment in comments:
    scraped_data.append((comment.text.strip(),))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(scraped_data)