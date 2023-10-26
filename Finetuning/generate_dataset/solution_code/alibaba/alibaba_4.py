import csv
import os
from lxml import html

# Load the HTML file
file_path = 'downloaded_pages/alibaba.html'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Extract the text from the search-card-m-sale-features__item divs
div_elements = tree.xpath('//div[@class="search-card-m-sale-features__item"]')
data = [div.text_content().strip() for div in div_elements]

# Save the scraped data as a CSV file
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    for item in data:
        writer.writerow([item])

print("Data scraped and saved successfully!")