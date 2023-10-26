import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/bbc.html') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all the article titles about Sir Patrick Stewart's bookshop visit
article_titles = tree.xpath("//h3[contains(@class, 'gs-c-promo-heading__title') and contains(text(), 'Sir Patrick Stewart makes surprise bookshop visit')]/text()")

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Article Title'])
    for title in article_titles:
        writer.writerow([title])