import csv
from lxml import etree

# Open the HTML file
with open("downloaded_pages/flyingtiger.html", "r") as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all h3 tags
h3_tags = tree.xpath("//h3")

# Extract the text from the h3 tags
texts = [tag.text.strip() for tag in h3_tags]

# Save the scraped data as CSV
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Scraped Text"])
    writer.writerows([[text] for text in texts])