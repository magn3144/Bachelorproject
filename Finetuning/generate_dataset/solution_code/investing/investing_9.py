import csv
from lxml import etree

# Load the HTML file
html_path = "downloaded_pages/investing.html"
with open(html_path, 'r') as file:
    html = file.read()

# Parse HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find all stock broker elements on the page
broker_elements = tree.xpath('//a[contains(@class, "inv-link") and contains(@class, "navbar_multi_list_link")]')

# Extract the names of the stock brokers
brokers = [broker.text.strip() for broker in broker_elements]

# Save the data as a CSV file
csv_path = "scraped_data.csv"
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([["Stock Brokers"], *[[broker] for broker in brokers]])