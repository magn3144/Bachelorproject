import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/bbc.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Create an element tree from the HTML content
tree = etree.HTML(html_content)

# Find all articles related to workplace toxicity
article_elements = tree.xpath("//h3[contains(@class, 'nw-o-link-split__text') and contains(text(), 'workplace toxicity')]/ancestor::div[@class='gs-c-promo']")

# Extract the titles of the articles
article_titles = [element.xpath(".//h3[contains(@class, 'gs-c-promo-heading__title')]/text()")[0] for element in article_elements]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title'])
    writer.writerows([[title] for title in article_titles])