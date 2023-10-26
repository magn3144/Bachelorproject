import csv
from lxml import html

# Define the HTML file path
html_file = 'downloaded_pages/ebay.html'

# Load the HTML file
with open(html_file, 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Retrieve the text for "Jamaica"
jamaica_text = tree.xpath('/html/body/div[4]/div[4]/div[3]/section/div[1]/div[2]/div[1]/div/div/form/div[1]/div/span/div/div[98]/span/text()')[0]

# Prepare the scraped data
data = [['Country', 'Text'],
        ['Jamaica', jamaica_text]]

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)