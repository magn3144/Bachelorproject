import csv
from lxml import html

# Read the local HTML file
with open('downloaded_pages/data.cdc.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Extract the result timestamps
result_timestamps = tree.xpath('//div[@class="browse2-result-timestamp-label"]/text()')

# Save the result timestamps as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Result Timestamps'])
    writer.writerows([[timestamp.strip()] for timestamp in result_timestamps])