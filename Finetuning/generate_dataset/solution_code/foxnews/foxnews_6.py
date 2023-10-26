import csv
from lxml import html

# Load the HTML file
with open("downloaded_pages/foxnews.html", "r") as file:
    html_string = file.read()

# Parse the HTML string
tree = html.fromstring(html_string)

# Find all page elements labelled as 'sponsored'
sponsored_elements = tree.xpath("//*[contains(@class, 'sponsored')]")

# Create a list to store the details of the sponsored elements
scraped_data = []

# Extract the details of the sponsored elements
for element in sponsored_elements:
    tag = element.tag
    text = element.text_content().strip()
    scraped_data.append((tag, text))

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Tag", "Text"])
    writer.writerows(scraped_data)