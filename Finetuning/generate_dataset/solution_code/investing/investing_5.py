import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/investing.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Get all investment funds
investment_funds = tree.xpath('//a[contains(@class, "inv-link")]/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for fund in investment_funds:
        writer.writerow([fund])