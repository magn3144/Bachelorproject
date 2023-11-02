import csv
from pathlib import Path
from lxml import html

# Define the XPath expressions for the elements
xpath_expressions = {
    "article_title": '//h1[@class="News__Item__Headline"]/text()',
    "article_description": '//div[@class="News__Item__Description"]/text()'
}

# Load the HTML file
html_file = Path('downloaded_pages/espn.html').read_text()

# Parse the HTML content
tree = html.fromstring(html_file)

# Scrape the data using XPath expressions
article_titles = tree.xpath(xpath_expressions["article_title"])
article_descriptions = tree.xpath(xpath_expressions["article_description"])

# Combine the scraped data into a list
scraped_data = list(zip(article_titles, article_descriptions))

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Article Title', 'Article Description'])
    writer.writerows(scraped_data)