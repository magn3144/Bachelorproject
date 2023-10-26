import csv
from lxml import etree

# Define the HTML file path
html_file_path = 'downloaded_pages/boardgamegeek.html'

# Define the XPath expressions for the search categories and labels
search_category_xpath = '//form//label[@class="tw-sr-only"]/text()'
search_label_xpath = '//form//label[@class="tw-sr-only"]//following-sibling::node()/text()'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file_path, parser)

# Extract the search categories and labels
search_categories = tree.xpath(search_category_xpath)
search_labels = tree.xpath(search_label_xpath)

# Create a list of dictionaries containing the scraped data
scraped_data = []
for category, label in zip(search_categories, search_labels):
    scraped_data.append({'Category': category.strip(), 'Label': label.strip()})

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Category', 'Label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)