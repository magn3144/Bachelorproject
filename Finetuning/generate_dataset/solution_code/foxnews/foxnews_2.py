import csv
from lxml import etree

# Open the HTML file
with open("downloaded_pages/foxnews.html", "r") as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all the 'other' elements
other_elements = tree.xpath("/html/body/div/header/div[4]/div[2]/div/nav[11]/h4")

# Extract the text from the 'other' elements
other_text = [element.text.strip() for element in other_elements]

# Save the data to a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows([[text] for text in other_text])