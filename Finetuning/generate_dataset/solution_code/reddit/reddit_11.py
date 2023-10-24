import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/reddit.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find all tip actions
tip_actions = tree.xpath('//span[contains(@class, "reddit-actionButton")]/text()')

# Save the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tip Actions'])
    for action in tip_actions:
        writer.writerow([action])