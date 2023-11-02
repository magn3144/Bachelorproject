import csv
import os
from lxml import etree

# Define the XPath expressions for the video titles and links
title_xpath = '//span[@class="QuickLinks__Item__Title"]'
link_xpath = '//a[@class="QuickLinks__Item__Title"]/@href'

# Load the HTML file
html_file = os.path.join('downloaded_pages', 'espn.html')
tree = etree.parse(html_file)
root = tree.getroot()

# Scrape the video titles and links
titles = root.xpath(title_xpath)
links = root.xpath(link_xpath)

# Combine the titles and links into a list of pairs
data = list(zip(titles, links))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Link'])
    writer.writerows(data)