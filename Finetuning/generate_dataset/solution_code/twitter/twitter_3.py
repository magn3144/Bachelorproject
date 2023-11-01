import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/twitter.html', 'r') as file:
    content = file.read()

# Parse the HTML content
tree = html.fromstring(content)

# Scrape the text from the specified XPath
text_elements = tree.xpath('/html/body/noscript/div/p[3]/a[2]/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Scraped Data'])
    writer.writerow(text_elements)