import csv
from lxml import etree

# Define the XPath expressions for the title and author of each article
title_xpath = "//h1[@class='header__title']"
author_xpath = "//span[@class='author']"

# Read the HTML file
html_file = "downloaded_pages/microsoft.html"
with open(html_file, "r") as f:
    html_data = f.read()

# Parse the HTML data
parser = etree.HTMLParser()
tree = etree.fromstring(html_data, parser)

# Extract the title and author of each article
articles = tree.xpath("//div[@class='article']")
data = []
for article in articles:
    title = article.xpath(title_xpath)
    author = article.xpath(author_xpath)
    if title and author:
        data.append({"Title": title[0].text.strip(), "Author": author[0].text.strip()})

# Save the scraped data as a CSV file
output_file = "scraped_data.csv"
header = ["Title", "Author"]
with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)