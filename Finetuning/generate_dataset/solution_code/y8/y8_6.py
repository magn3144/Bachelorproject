import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/y8.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the category
category_element = tree.xpath('/html/body/div[1]/div[1]/div/div[1]/div/ul/li[13]')[0]
category = category_element.text.strip()

# Save the category to CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category'])
    writer.writerow([category])