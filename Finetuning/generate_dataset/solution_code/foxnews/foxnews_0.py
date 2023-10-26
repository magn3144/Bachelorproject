import csv
from lxml import etree

# Define the target HTML file path
html_file = 'downloaded_pages/foxnews.html'

# Define the category
category = 'News'

# Define the XPath for headlines in the News category
headline_xpath = '//h3[contains(@class, "title")]/text()'

# Scrape the headlines
tree = etree.parse(html_file)
headlines = tree.xpath(headline_xpath)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category', 'Headline'])
    for headline in headlines:
        writer.writerow([category, headline])