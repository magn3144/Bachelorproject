import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/seekingalpha.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find all navigation items in the header
navigation_items = tree.xpath('/html/body/div[2]/div/div[1]/div/header/div[1]/div[2]/nav//a')

# Scrape the text from each navigation item
navigation_text = [item.text_content() for item in navigation_items]

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Navigation Item'])
    writer.writerows([[item] for item in navigation_text])