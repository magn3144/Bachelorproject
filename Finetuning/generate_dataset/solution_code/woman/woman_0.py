import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/woman.html', 'r') as file:
    html = file.read()

# Create an ElementTree object
tree = etree.HTML(html)

# Initialize the list to store scraped data
data = []

# Get all the blog titles and categories
titles = tree.xpath("//h3[contains(text(), 'Flere blogindlæg')]/following-sibling::div//a/text()")
categories = ['Blogs'] * len(titles)

# Combine the titles and categories into a list of tuples
data = list(zip(titles, categories))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Category'])
    writer.writerows(data)