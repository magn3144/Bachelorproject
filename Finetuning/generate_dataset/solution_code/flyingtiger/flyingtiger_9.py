import csv
from lxml import etree

# Define the HTML file path
html_file = "downloaded_pages/flyingtiger.html"

# Read the HTML file
with open(html_file, "r") as file:
    html_content = file.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Find all <li> elements
li_elements = html_tree.xpath("//li")

# Extract the text inside <li> elements
scraped_data = [li.text.strip() for li in li_elements]

# Save the scraped data as CSV
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Text"])
    writer.writerows([[data] for data in scraped_data])