import csv
from lxml import etree

# Read the HTML file
html_file = "downloaded_pages/microsoft.html"
with open(html_file, "r") as file:
    html_content = file.read()

# Parse the HTML content
parser = etree.HTMLParser()
tree = etree.fromstring(html_content, parser)

# Retrieve the names of services under the "Outlook" category
services = tree.xpath('//div[contains(text(), "Outlook")]/following-sibling::ul/li')
service_names = [service.text.strip() for service in services]

# Save the scraped data as CSV
csv_file = "scraped_data.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Service Name"])
    writer.writerows([[name] for name in service_names])