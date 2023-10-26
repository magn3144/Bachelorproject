from lxml import html
import csv

# Open the HTML file
with open('downloaded_pages/redfin.html', 'r') as file:
    html_content = file.read()

# Create an HTML tree from the file content
tree = html.fromstring(html_content)

# Find all anchor elements
anchor_elements = tree.xpath('//a')

# Extract the text and URLs from the anchor elements
data = []
for anchor in anchor_elements:
    text = anchor.text_content()
    url = anchor.get('href')
    data.append([text, url])

# Save the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text', 'URL'])
    writer.writerows(data)