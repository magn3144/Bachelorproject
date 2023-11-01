import csv
from lxml import etree
from io import StringIO, BytesIO

# Load the HTML file
with open("downloaded_pages/y8.html", "r") as file:
    html_content = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.parse(StringIO(html_content), parser)

# Find the username element
username_element = tree.xpath("/html/body/nav/div[1]/div[2]/div[5]/div[2]/div[2]/div/div[1]/span[1]")[0]

# Extract the username
username = username_element.text.strip()

# Save the username as a CSV file
with open("scraped_data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Username'])
    writer.writerow([username])