import csv
from lxml import etree

# Define the HTML file path
html_file = 'downloaded_pages/washingtonpost.html'

# Define the XPaths for the article titles and authors
title_xpath = '//h3[contains(@class, "font-md") and contains(@class, "font-bold") and contains(@class, "font--headline")]/text()'
author_xpath = '//span[contains(@class, "wpds-c-knSWeD")]/text()'

# Create a list to store the scraped data
scraped_data = []

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Extract the article titles
titles = tree.xpath(title_xpath)

# Extract the authors
authors = tree.xpath(author_xpath)

# Combine the titles and authors into tuples
data = zip(titles, authors)

# Add the data to the scraped_data list
scraped_data.extend(data)

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(scraped_data)