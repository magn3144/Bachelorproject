import csv
from lxml import etree

# Read the HTML file
with open("downloaded_pages/textures.html", "r") as file:
    html = file.read()

# Parse HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find all texture license types and their details
license_types = tree.xpath("//div[@class='category'][contains(text(),'Digital Websites')]/following-sibling::div[@class='col-md-12']//h3")
license_details = tree.xpath("//div[@class='category'][contains(text(),'Digital Websites')]/following-sibling::div[@class='col-md-12']//p")

# Create a list of dictionaries to hold the scraped data
scraped_data = []
for license_type, license_detail in zip(license_types, license_details):
    scraped_data.append({"License Type": license_type.text, "License Detail": license_detail.text})

# Save the scraped data as CSV
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["License Type", "License Detail"])
    writer.writeheader()
    writer.writerows(scraped_data)