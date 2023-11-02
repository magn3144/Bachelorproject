import csv
from lxml import html

# Read the HTML file and parse it
with open('downloaded_pages/washingtonpost.html', 'r', encoding='utf-8') as f:
    html_data = f.read()

tree = html.fromstring(html_data)

# Find all subscription newsletter titles and descriptions using XPath
titles = tree.xpath('//div[contains(@class, "wpds-c-fJKSbB")]/text()')
descriptions = tree.xpath('//span[contains(@class, "items-center")]/text()')

# Zip titles and descriptions together
data = zip(titles, descriptions)

# Save data as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Description'])  # Write header
    writer.writerows(data)  # Write data rows