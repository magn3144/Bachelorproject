
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find all the header buttons
buttons = tree.xpath('//header/div[2]/div/div/button')

# Create a list to store the scraped data
scraped_data = []

# Loop over the buttons and extract the text
for button in buttons:
    scraped_data.append([button.text])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(scraped_data)
