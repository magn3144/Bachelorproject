from lxml import html
import csv

# Open the HTML file
with open('downloaded_pages/edx.html', 'r') as file:
    content = file.read()

# Parse the HTML content
tree = html.fromstring(content)

# Find the AI project manager paragraph using the XPath
paragraph = tree.xpath('/html/body/div[1]/div[1]/div/main/div/div[7]/div/div/div[3]/div/div/div[1]/ul[1]/li[2]/p')[0].text_content()

# Save the paragraph as CSV
with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([paragraph])