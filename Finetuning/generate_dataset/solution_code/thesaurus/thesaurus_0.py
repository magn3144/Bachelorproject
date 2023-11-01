import csv
from lxml import html

# Define the XPath expressions for the article titles and URLs
title_xpath = '//h2[contains(@class, "bGXYJrRLH25ON04NlCTo")]'
url_xpath = '//a[contains(@class, "swOceu30Ur0oywqmOgSd")]/@href'

# Get the HTML content from the file
with open('downloaded_pages/thesaurus.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Extract the article titles and URLs
titles = tree.xpath(title_xpath)
urls = tree.xpath(url_xpath)

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'URL'])
    writer.writerows(zip(titles, urls))