import csv
from lxml import html

# Define the path to the HTML file
html_path = 'downloaded_pages/tumblr.html'

# Read the HTML file
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Extract the number of reblogs for each post
reblogs_elements = tree.xpath('//div[contains(@class, "rZlUD W45iW")]')
reblogs_counts = [element.text.strip() for element in reblogs_elements]

# Save the scraped data to CSV file
csv_path = 'scraped_data.csv'
with open(csv_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Post', 'Reblogs'])
    for i, count in enumerate(reblogs_counts):
        writer.writerow([f'Post {i+1}', count])