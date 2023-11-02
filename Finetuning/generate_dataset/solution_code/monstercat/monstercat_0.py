import csv
import os
from lxml import html

# Read the HTML file
file_path = 'downloaded_pages/monstercat.html'
with open(file_path, 'r') as f:
    content = f.read()

# Parse the HTML content
tree = html.fromstring(content)

# Scrape the discography table
table_rows = tree.xpath('/html/body/div[4]/div[4]/div[3]/main/div[3]/div/div/table/tbody/tr')

# Extract the album names and release dates
data = []
for row in table_rows:
    album_name = row.xpath('./td[2]/a/text()')[0]
    release_date = row.xpath('./td[4]/text()')[0]
    data.append([album_name, release_date])

# Save the scraped data as CSV
csv_file = 'scraped_data.csv'
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Album Name', 'Release Date'])
    writer.writerows(data)

print("Scraping completed and data saved as 'scraped_data.csv'.")