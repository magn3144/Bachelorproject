import csv
from pathlib import Path
from lxml import html

# Define the target HTML file path
html_file_path = 'downloaded_pages/youtube-comments.html'

# Load the HTML page
with open(html_file_path, 'r', encoding='utf-8') as file:
    page_content = file.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Extract the number of views using XPath
views_element = tree.xpath('//span[@class="inline-metadata-item style-scope ytd-video-meta-block"]/text()')[0]
views = views_element.strip()

# Create a list to hold the data
data = [['Category', 'Number of Views'],
        ['Social Media', views]]

# Save the data as a CSV file
csv_path = 'scraped_data.csv'
with open(csv_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)