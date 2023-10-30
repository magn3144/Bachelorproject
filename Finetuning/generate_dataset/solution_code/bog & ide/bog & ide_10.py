import csv
from lxml import etree

# Define the XPaths
xpath = "/html/body/div/main/div[1]/div[2]/div/div[3]/div/div[1]/h4"

# Load the HTML file
with open("downloaded_pages/bog & ide.html", 'r', encoding="utf-8") as f:
    html_content = f.read()

# Parse the HTML
tree = etree.HTML(html_content)

# Find the heading text
heading = tree.xpath(xpath)[0].text.strip()

# Create a list with the extracted data
data = [heading]

# Save the data as CSV
with open('scraped_data.csv', 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Heading"])
    writer.writerow(data)