import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/nytimes.html', 'r') as file:
    html = file.read()

# Create an lxml element tree from the HTML
tree = etree.HTML(html)

# Find the articles in the "Arts" section
articles = tree.xpath('/html/body/div/div[2]/nav/div/div[2]/div/section[3]/h3/following-sibling::ul[1]/li/a')

# Extract the titles of the articles
titles = [article.text for article in articles]

# Save the titles as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerows(zip(titles))