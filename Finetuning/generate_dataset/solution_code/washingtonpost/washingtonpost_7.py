import csv
from lxml import etree

# Define the target HTML file path
html_file = 'downloaded_pages/washingtonpost.html'

# Define the target category
category = 'News'

# Define the XPath expressions for technology-related article titles and authors
title_xpath = '//h3[contains(@class, "font--headline")]/text()'
author_xpath = '//a[contains(@class, "wpds-c-knSWeD")]/text()'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Extract the title and author information
titles = tree.xpath(title_xpath)
authors = tree.xpath(author_xpath)

# Zip the scraped data
scraped_data = zip(titles, authors)

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Author'])  # Write the header row
    writer.writerows(scraped_data)  # Write the data rows