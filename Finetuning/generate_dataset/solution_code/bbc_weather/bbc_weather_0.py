import csv
from lxml import etree

# Load the HTML file
html_path = "downloaded_pages/bbc_weather.html"
with open(html_path, "r") as f:
    html_content = f.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.parse(html_path, parser)

# Define the XPaths for the target elements
xpath_external_linking = "/html/body/div[9]/footer/div/div/div/small/span/a"

# Extract the information from the target elements
external_linking_element = tree.xpath(xpath_external_linking)[0]
external_linking_text = external_linking_element.text

# Write the information to the CSV file
csv_path = "scraped_data.csv"
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Approach to External Linking"])
    writer.writerow([external_linking_text])