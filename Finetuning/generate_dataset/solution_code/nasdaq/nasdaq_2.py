from lxml import etree
import csv

# Load the HTML file
html_path = 'downloaded_pages/nasdaq.html'
with open(html_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content
html = etree.HTML(html_content)

# Retrieve all the DIV elements containing information about the market calendar
market_divs = html.xpath('//div[contains(@class, "market-calendar-table__cell-content")]')

# Write the scraped data to a CSV file
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Market Calendar Info'])
    for div in market_divs:
        writer.writerow([div.text.strip()])

print(f"Scraped data has been saved as '{csv_file_path}'")