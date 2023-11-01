import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/jysk.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
page = html.fromstring(html_content)

# Find all B2B customers on the page
b2b_customers = page.xpath('//span[contains(text(), "B2B Kunde")]/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['B2B Customer'])
    writer.writerows([[customer] for customer in b2b_customers])