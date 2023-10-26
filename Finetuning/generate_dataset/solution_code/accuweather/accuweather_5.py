import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/accuweather.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Scrape the index status text
index_status_text = tree.xpath('/html/body/div/div[7]/div[1]/div[1]/div[2]/div[2]/div[3]/a[1]/div[4]/text()')[0]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['index_status_text'])
    writer.writerow([index_status_text])