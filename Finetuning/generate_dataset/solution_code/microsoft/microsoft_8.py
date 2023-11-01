import csv
from lxml import html

# Define the target file path
file_path = 'downloaded_pages/microsoft.html'

# Define the XPath for the educational categories
category_xpath = '//h3[contains(@class, "HubPageTrendingTopicsCategoryHeading")]/text()'

# Parse the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    page_content = file.read()
tree = html.fromstring(page_content)

# Scrape the educational categories
categories = tree.xpath(category_xpath)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category'])
    writer.writerows(zip(categories))