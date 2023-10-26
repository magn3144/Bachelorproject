import csv
from lxml import html

# Read HTML file
with open('downloaded_pages/ebay.html', 'r') as file:
    html_content = file.read()

# Parse HTML content
tree = html.fromstring(html_content)

# Scrape the "Enter zip code" label
enter_zip_code_label = tree.xpath('/html/body/div[4]/div[4]/div[3]/section/div[1]/div[2]/div[1]/div/div/form/div[2]/span/label/text()')[0]

# Save scraped data to CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Enter Zip Code'])
    writer.writerow([enter_zip_code_label])