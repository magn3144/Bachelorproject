import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/britannica.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find all article titles related to autumn
article_titles = tree.xpath("//p[contains(., 'autumn')]/text()")

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerows(zip(article_titles))